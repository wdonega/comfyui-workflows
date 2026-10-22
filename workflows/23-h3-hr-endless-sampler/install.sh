#!/usr/bin/env bash
# H3 HR Endless Sampler (Gemma 4 dirige os chunks): instala custom nodes e modelos no ComfyUI.
# Gerado por tools/gen.py a partir de components.json. Não edite à mão.
#
# Uso:  bash install.sh /caminho/do/ComfyUI        (ou COMFYUI_DIR=... bash install.sh)
# Docker: docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < install.sh

# Funções comuns dos install.sh (o gerador embute este arquivo em cada script).
# Variáveis: COMFYUI_DIR (raiz do ComfyUI), HF_TOKEN (repos gated), VERIFY_EXISTING=1 (confere SHA-256
# de arquivos já presentes; por padrão só o tamanho é conferido e o hash só é verificado em downloads novos).

set -euo pipefail

log() { printf '\033[1;34m[comfy-install]\033[0m %s\n' "$*"; }
ok() { printf '  \033[1;32m✓\033[0m %s\n' "$*"; }
warn() { printf '  \033[1;33m!\033[0m %s\n' "$*"; }
die() { printf '\033[1;31m[erro]\033[0m %s\n' "$*" >&2; exit 1; }

# Guardrail: COMFYUI_DIR precisa ser a raiz do ComfyUI (main.py + models/ + custom_nodes/).
comfy_root() {
    local dir="${1:-${COMFYUI_DIR:-$PWD}}"
    dir="$(cd "$dir" 2>/dev/null && pwd)" || die "pasta não existe: ${1:-${COMFYUI_DIR:-$PWD}}"
    if [[ -f "$dir/main.py" && -f "$dir/folder_paths.py" && -d "$dir/models" && -d "$dir/custom_nodes" ]]; then
        COMFYUI_DIR="$dir"
        log "ComfyUI em $COMFYUI_DIR"
        return
    fi
    # dica: se estamos dentro de um ComfyUI, aponta a raiz
    local up="$dir"
    while [[ "$up" != "/" ]]; do
        up="$(dirname "$up")"
        if [[ -f "$up/main.py" && -d "$up/models" && -d "$up/custom_nodes" ]]; then
            die "$dir está DENTRO do ComfyUI. Rode na raiz: COMFYUI_DIR=$up (ou passe $up como argumento)"
        fi
    done
    die "$dir não é a raiz do ComfyUI (precisa ter main.py, folder_paths.py, models/ e custom_nodes/). Passe a pasta certa como argumento ou em COMFYUI_DIR."
}

# fetch_model <pasta em models/> <arquivo> <url> <sha256|-> <tamanho|->
fetch_model() {
    local dest="$1" file="$2" url="$3" sha="$4" size="$5"
    local dir="$COMFYUI_DIR/models/$dest" target="$COMFYUI_DIR/models/$dest/$file"
    mkdir -p "$dir"
    if [[ -f "$target" ]]; then
        local have; have=$(stat -c %s "$target")
        if [[ "$size" != "-" && "$have" != "$size" ]]; then
            warn "$dest/$file existe mas tem $have bytes (esperado $size): não mexo; apague e rode de novo"
            return
        fi
        if [[ "${VERIFY_EXISTING:-0}" == 1 && "$sha" != "-" ]]; then
            [[ "$(sha256sum "$target" | cut -d' ' -f1)" == "$sha" ]] || die "$dest/$file: SHA-256 não confere"
        fi
        ok "$dest/$file (já existe)"
        return
    fi
    log "baixando $dest/$file"
    local auth=()
    [[ -n "${HF_TOKEN:-}" && "$url" == https://huggingface.co/* ]] && auth=(-H "Authorization: Bearer $HF_TOKEN")
    curl -fL --progress-bar --retry 3 -C - "${auth[@]}" -o "$target.part" "$url" \
        || die "falha ao baixar $url (repo gated? aceite a licença na página e exporte HF_TOKEN)"
    if [[ "$sha" != "-" ]]; then
        [[ "$(sha256sum "$target.part" | cut -d' ' -f1)" == "$sha" ]] || { rm -f "$target.part"; die "$file: SHA-256 não confere"; }
    fi
    mv "$target.part" "$target"
    ok "$dest/$file"
}

# link_model <pasta em models/> <caminho do link> <alvo relativo à pasta do link>
link_model() {
    local dest="$1" link="$2" target="$3"
    local path="$COMFYUI_DIR/models/$dest/$link"
    mkdir -p "$(dirname "$path")"
    if [[ -e "$path" || -L "$path" ]]; then ok "$dest/$link (link já existe)"; return; fi
    ln -s "$target" "$path"
    ok "$dest/$link -> $target"
}

# registry_node <id no registro do ComfyUI> <versão>  (mesmo formato que o ComfyUI-Manager instala)
registry_node() {
    local id="$1" version="$2" dir="$COMFYUI_DIR/custom_nodes/$1"
    if [[ -d "$dir" ]]; then
        local have; have=$(grep -m1 '^version' "$dir/pyproject.toml" 2>/dev/null | cut -d'"' -f2 || true)
        if [[ "$have" == "$version" ]]; then ok "custom_nodes/$id ($have)"
        else warn "custom_nodes/$id já existe (${have:-versão desconhecida}; testado em $version); não alterei"; fi
        return
    fi
    log "instalando $id $version do registro"
    local zip; zip="$(mktemp --suffix=.zip)"
    local publisher; publisher="$(curl -fsS "https://api.comfy.org/nodes/$id" | python3 -c 'import json,sys;print(json.load(sys.stdin)["publisher"]["id"])')"
    curl -fsSL -o "$zip" "https://cdn.comfy.org/$publisher/$id/$version/node.zip" || die "falha ao baixar $id $version"
    mkdir -p "$dir" && python3 -c 'import sys,zipfile;zipfile.ZipFile(sys.argv[1]).extractall(sys.argv[2])' "$zip" "$dir"
    rm -f "$zip"
    ok "custom_nodes/$id ($version)"
}

# clone_node <url git> <commit>
clone_node() {
    local url="$1" commit="$2" name; name="$(basename "$url" .git)"
    local dir="$COMFYUI_DIR/custom_nodes/$name"
    if [[ -d "$dir" ]]; then
        local have; have=$(git -C "$dir" rev-parse --short HEAD 2>/dev/null || echo "sem git")
        if [[ "$have" == "${commit:0:7}" ]]; then ok "custom_nodes/$name ($have)"
        else warn "custom_nodes/$name já existe em $have (testado em ${commit:0:7}); não alterei"; fi
        return
    fi
    log "clonando $name"
    git clone -q "$url" "$dir"
    git -C "$dir" checkout -q "$commit"
    ok "custom_nodes/$name (${commit:0:7})"
    if [[ -f "$dir/requirements.txt" ]]; then
        warn "$name tem requirements.txt: instale no Python do ComfyUI (veja o README desta pasta)"
    fi
}

comfy_root "${1:-}"
registry_node comfyui-kjnodes 1.5.0
registry_node comfyui-videohelpersuite 1.7.9
clone_node https://github.com/hradec/ComfyUI-HR-Endless-Sampler 1681f89ac022371e5e12d565b1486ee104327621
fetch_model diffusion_models minimax_h3_ref2va_pruned_int8_convrot.safetensors https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors 9255f52b6677845ad238f20dfaafa94727053694127ab7f255c048f0f9365779 20970379616
fetch_model text_encoders qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors 35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6 15687142551
fetch_model vae minimax_h3_video_vae_fp16.safetensors https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_fp16.safetensors 7c1f131492e7eddacaac9069a61b81bdd39de5cc96561e677c5eab1cdce5e522 5207808496
fetch_model vae minimax_h3_audio_vae_fp32.safetensors https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors 8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48 605254808
fetch_model llama_cpp/gemma-4-12b-it-qat-q4_0 gemma-4-12b-it-qat-q4_0.gguf https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf/resolve/29d097773436b69ff9feafd636ab4cf873786537/gemma-4-12b-it-qat-q4_0.gguf 93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b 6975879296
fetch_model llama_cpp/gemma-4-12b-it-qat-q4_0 mmproj-gemma-4-12b-it-qat-q4_0.gguf https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf/resolve/29d097773436b69ff9feafd636ab4cf873786537/mmproj-gemma-4-12b-it-qat-q4_0.gguf cb018338a7538a9814d994bfe54644c71eb7ed54e31eae2f721e45fd3c260da7 175115616
fetch_model llama_cpp/gemma-4-12b-it-qat-q4_0 gemma-4-12B-it-qat-assistant-MTP-Q8_0.gguf https://huggingface.co/Janvitos/gemma-4-12B-it-qat-assistant-MTP-Q8_0-GGUF/resolve/f5fdc2cdfa1a1257cf6d979fb17f1c94f9852ec4/gemma-4-12B-it-qat-assistant-MTP-Q8_0.gguf 13331068b6af643c3dc75e619373b674c1f75a1958e7c82e2020d96a17c63809 465127040
fetch_model vae_approx taeh3.safetensors https://github.com/madebyollin/taehv/raw/011dfc2112197741c540e0bdd5b7b67bcc930771/safetensors/taeh3.safetensors 4fd022bfcab08772fe0536b17ea1a3bbb5625be11e397868d1c5d891863d4c13 22709752
log "pronto. Reinicie o ComfyUI se instalou custom nodes novos."
