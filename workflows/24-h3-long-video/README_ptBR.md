# H3 Long Video (prompt dividido por LLM)

[comfyui-workflows](../../README_ptBR.md) › **H3 Long Video (prompt dividido por LLM)**

Gera vídeos mais longos que um único sampling do H3 encadeando segmentos que continuam movimento e áudio. Um LLM (qualquer servidor compatível com a API da OpenAI; no teste, um llama.cpp local em outra GPU) divide a história em prompts por segmento com o tempo certo. Usa Ref2VA + LoRA Ref2V Turbo 8 steps e atenção esparsa (`BlockSparseAttention`).

| | |
|---|---|
| Status | ✅ testado |
| Família | MiniMax H3 |
| Licença | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Download total | 44.43 GB |
| Teste | 16 s em 2 segmentos de 8 s, 960x544, 8 steps, 1 referência; LLM qwen3.8-flash-next (llama.cpp local, outra GPU) dividiu a história corretamente (fala no 2º segmento); emenda contínua, identidade consistente, áudio contínuo |
| Tempo | **11min 27s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15659 MiB |

## Arquivos desta pasta

| Arquivo | O que é |
|---|---|
| `workflow.json` | Workflow para arrastar na interface do ComfyUI |
| `workflow.api.json` | Mesmo workflow no formato da API (parâmetros do teste, entradas de exemplo) |
| `install.sh` | Instala custom nodes e baixa os modelos para as pastas certas |
| `components.json` | Fonte dos dados deste README e do install.sh |

## Instalação

```bash
# na máquina com o ComfyUI (o script confere se a pasta é a raiz do ComfyUI)
bash install.sh /path/to/ComfyUI

# ComfyUI em Docker (container "comfyui")
docker exec -i -e HF_TOKEN comfyui bash -s -- /root/ComfyUI < install.sh
```

Arquivos que já existem com o tamanho certo são pulados. Downloads novos têm o SHA-256 conferido (`VERIFY_EXISTING=1` confere também os que já existiam).

## Custom nodes

| Nó | Versão testada | Página |
|---|---|---|
| ComfyUI-H3-Long-Video | `7499153` | https://github.com/ooizj/ComfyUI-H3-Long-Video |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | modelo Ref2VA (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | text encoder Qwen3-VL 32B (NVFP4) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_fp16.safetensors` | VAE de vídeo fp16 | 5.21 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_fp16.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | VAE de áudio | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `loras/` | `minimax_h3_ref2v_turbo_8step_v1.1_768p_comfyui_bf16.safetensors` | LoRA Ref2V Turbo 8 steps v1.1 (força 0.8) | 1.96 GB | [download](https://huggingface.co/lightx2v/Minimax-h3-Turbo/resolve/30f485ed874aa44c8183348ad361c5eabad318da/minimax_h3_ref2v_turbo_8step_v1.1_768p_comfyui_bf16.safetensors) | [página](https://huggingface.co/lightx2v/Minimax-h3-Turbo) |

<details><summary>SHA-256</summary>

```
9255f52b6677845ad238f20dfaafa94727053694127ab7f255c048f0f9365779  models/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
7c1f131492e7eddacaac9069a61b81bdd39de5cc96561e677c5eab1cdce5e522  models/vae/minimax_h3_video_vae_fp16.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
e56863a7524e0300729cbb7b64cc8b548d90698c1abbf7d83898b0122fbe1e81  models/loras/minimax_h3_ref2v_turbo_8step_v1.1_768p_comfyui_bf16.safetensors
```

</details>

## Como usar

1. No **Ref Prompt Builder**, escolha as imagens de referência (`pictures`) e escreva a história inteira; cite `<Picture 1>` etc.
2. No **H3 Prompt API**: `api_url` = servidor compatível com OpenAI (`http://localhost:8080/v1` neste arquivo; DeepSeek no original do autor), `model` do servidor. `max_tokens` com folga se o modelo "pensa" antes de responder.
3. No **H3 Long Video**: `total_seconds` (duração final) e `segment_seconds` (tamanho de cada segmento). Mais de um segmento exige o Prompt API conectado.
4. `local_llm` = `auto`: só descarrega os modelos do ComfyUI se a URL for localhost. Se o seu LLM roda em outra máquina ou GPU, use o endereço dela e nada é descarregado.

## Licença

Uso pessoal e comercial liberados até US$ 20 mi/ano de receita (acima disso, autorização da MiniMax). **Proibido nos EUA, UE, Reino Unido e Coreia do Sul, inclusive exibir ou distribuir as saídas lá (cláusula V.4)**: não use os vídeos em projetos publicados globalmente. Conteúdo publicado deve ser identificado como gerado por IA; proibido personificar pessoas reais sem consentimento; produto comercial deve exibir "MiniMax H3". LoRAs de terceiros herdam essas regras.

## Observações

- O log com os prompts de cada segmento fica em `output/h3_prompt_logs/`.
- O autor recomenda LLMs fortes (27B denso ou DeepSeek) para dividir falas cronometradas; o qwen3.8-flash-next (llama.cpp local) acertou no teste.
- Para o workflow da interface com a organização original do autor (subgraph), veja `example_workflows/` no repositório do nó.
