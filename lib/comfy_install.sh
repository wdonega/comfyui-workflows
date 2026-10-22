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
