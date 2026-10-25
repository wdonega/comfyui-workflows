# H3 HR Endless Sampler (Gemma 4 dirige os chunks)

[comfyui-workflows](../../README_ptBR.md) › **H3 HR Endless Sampler (Gemma 4 dirige os chunks)**

Substitui o `SamplerCustomAdvanced` por um sampler em chunks com continuação no latente. Um **Gemma 4 12B** local (llama.cpp) analisa o prompt e as referências, planeja os planos e escreve o prompt de cada chunk; os cortes `[Shot N] At MM:SS.mmm,` caem no frame exato. Ref2VA sem LoRA, 20 steps.

| | |
|---|---|
| Status | ✅ testado |
| Família | MiniMax H3 |
| Licença | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Download total | 50.11 GB |
| Teste | 6 s, 0,5 MP (960x544), chunks de 39 frames (5 chunks), 20 steps, 1 referência, 2 planos com corte em 00:03.000 (caiu no frame 72); identidade mantida. Do total: H3 508 s, Gemma 377 s |
| Tempo | **18min 38s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15583 MiB |

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
| KJNodes | 1.5.0 | https://github.com/kijai/ComfyUI-KJNodes |
| VideoHelperSuite | 1.7.9 | https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite |
| ComfyUI-HR-Endless-Sampler | `1681f89` | https://github.com/hradec/ComfyUI-HR-Endless-Sampler |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | modelo Ref2VA (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | text encoder Qwen3-VL 32B (NVFP4) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_fp16.safetensors` | VAE de vídeo fp16 | 5.21 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_fp16.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | VAE de áudio | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `llama_cpp/gemma-4-12b-it-qat-q4_0/` | `gemma-4-12b-it-qat-q4_0.gguf` | Gemma 4 12B QAT Q4_0 (diretor; Apache-2.0) | 6.98 GB | [download](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf/resolve/29d097773436b69ff9feafd636ab4cf873786537/gemma-4-12b-it-qat-q4_0.gguf) | [página](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf) |
| `llama_cpp/gemma-4-12b-it-qat-q4_0/` | `mmproj-gemma-4-12b-it-qat-q4_0.gguf` | projetor de visão do Gemma | 0.18 GB | [download](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf/resolve/29d097773436b69ff9feafd636ab4cf873786537/mmproj-gemma-4-12b-it-qat-q4_0.gguf) | [página](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf) |
| `llama_cpp/gemma-4-12b-it-qat-q4_0/` | `gemma-4-12B-it-qat-assistant-MTP-Q8_0.gguf` | drafter MTP (acelera o Gemma) | 0.47 GB | [download](https://huggingface.co/Janvitos/gemma-4-12B-it-qat-assistant-MTP-Q8_0-GGUF/resolve/f5fdc2cdfa1a1257cf6d979fb17f1c94f9852ec4/gemma-4-12B-it-qat-assistant-MTP-Q8_0.gguf) | [página](https://huggingface.co/Janvitos/gemma-4-12B-it-qat-assistant-MTP-Q8_0-GGUF) |
| `vae_approx/` | `taeh3.safetensors` | TAEH3: preview leve dos chunks (MIT, opcional) | 23 MB | [download](https://github.com/madebyollin/taehv/raw/011dfc2112197741c540e0bdd5b7b67bcc930771/safetensors/taeh3.safetensors) | [página](https://github.com/madebyollin/taehv) |

<details><summary>SHA-256</summary>

```
9255f52b6677845ad238f20dfaafa94727053694127ab7f255c048f0f9365779  models/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
7c1f131492e7eddacaac9069a61b81bdd39de5cc96561e677c5eab1cdce5e522  models/vae/minimax_h3_video_vae_fp16.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b  models/llama_cpp/gemma-4-12b-it-qat-q4_0/gemma-4-12b-it-qat-q4_0.gguf
cb018338a7538a9814d994bfe54644c71eb7ed54e31eae2f721e45fd3c260da7  models/llama_cpp/gemma-4-12b-it-qat-q4_0/mmproj-gemma-4-12b-it-qat-q4_0.gguf
13331068b6af643c3dc75e619373b674c1f75a1958e7c82e2020d96a17c63809  models/llama_cpp/gemma-4-12b-it-qat-q4_0/gemma-4-12B-it-qat-assistant-MTP-Q8_0.gguf
4fd022bfcab08772fe0536b17ea1a3bbb5625be11e397868d1c5d891863d4c13  models/vae_approx/taeh3.safetensors
```

</details>

## Como usar

1. Escreva o prompt com os planos no formato do nó: `[Shot 1] ...` e, a partir do segundo, `[Shot 2] At 00:03.000, ...` (tempo em MM:SS.mmm a 24 fps). Sem o `At`, o nó para com erro.
2. Duração em segundos no **PrimitiveFloat** ligado ao cálculo do `length`; resolução no **ResolutionSelector** (`megapixels`).
3. `chunk_frames`: 39 é um bom ponto de partida em 16 GB (menos VRAM, mais emendas).
4. As referências passam por **ImageScaleBy** (o template do autor usa 0.3 para imagens 4K; com imagens de ~800 px use 1.0).

## Licença

Uso pessoal e comercial liberados até US$ 20 mi/ano de receita (acima disso, autorização da MiniMax). **Proibido nos EUA, UE, Reino Unido e Coreia do Sul, inclusive exibir ou distribuir as saídas lá (cláusula V.4)**: não use os vídeos em projetos publicados globalmente. Conteúdo publicado deve ser identificado como gerado por IA; proibido personificar pessoas reais sem consentimento; produto comercial deve exibir "MiniMax H3". LoRAs de terceiros herdam essas regras.

## Observações

- **Precisa do `llama-cpp-python` 0.3.35 com CUDA**, instalado no Python do ComfyUI. O wheel oficial (cu125) é compilado com AVX-512 e dá *Illegal instruction* em CPUs sem AVX-512; aqui foi compilado do código-fonte com `-DGGML_CUDA=on -DCMAKE_CUDA_ARCHITECTURES=120 -DGGML_NATIVE=OFF -DGGML_AVX2=ON -DGGML_AVX512=OFF` contra CUDA 13 (as libs cu13 do ComfyUI). Instale com `--no-deps` para não mexer no torch.
- O template do autor usa o nó **Spectrum** (`comfyui-spectrum-minimax-h3`, acelerador opcional). A versão mais recente dele está marcada (Flagged) no registro do ComfyUI; este workflow foi testado **sem** ele.
- O Gemma divide a GPU com o H3: neste teste ele levou 377 s dos 1118 s. `cache_gemma_preproduction` reaproveita o planejamento quando só a seed muda.
- O nó baixa o Gemma sozinho se faltar; o install.sh já deixa no lugar.
- **Efeito colateral:** o `pytorch_memory_fraction` (0,85) fica valendo para o **processo inteiro** do ComfyUI depois que o workflow termina. Na regressão, o Wan Animate 2 rodado em seguida deu falta de memória (limite de 13,2 GB numa placa de 16 GB). Reinicie o ComfyUI depois de usar o HR Endless, ou use 1.0.
