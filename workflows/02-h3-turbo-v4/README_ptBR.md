# H3 Turbo v4 (larryvrh)

[comfyui-workflows](../../README_ptBR.md) › **H3 Turbo v4 (larryvrh)**

O Ref2VA base com o **MiniMax-H3 Turbo LoRA** (checkpoint `v4_step600_ema`, recomendado pelo autor) e o **MiniMax-H3 Turbo Sampler**, no lugar do TaoMate. O sampler cuida das escalas separadas de vídeo e áudio. Faixa útil: 4 a 8 steps, scheduler `simple`.

| | |
|---|---|
| Item do plano | #2 |
| Status | ✅ testado |
| Família | MiniMax H3 |
| Licença | [MiniMax H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) |
| Download total | 40.85 GB |
| Teste | 736x1280, 362 frames (15 s), 6 steps, mesma cena/seed do workflow base: vídeo coerente, sem artefatos, fotografia mais escura e expressões mais dramáticas; ~2x mais lento que o TaoMate 3 steps |
| Tempo | **16min 48s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 15603 MiB |

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
| ComfyUI-MiniMax-H3-Turbo | `4274783` | https://github.com/Larryvrh/ComfyUI-MiniMax-H3-Turbo |

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | modelo Ref2VA (INT8) | 20.97 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | text encoder Qwen3-VL 32B (NVFP4, Blackwell) | 15.69 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_video_vae_int8_convrot.safetensors` | VAE de vídeo | 2.81 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_video_vae_int8_convrot.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `vae/` | `minimax_h3_audio_vae_fp32.safetensors` | VAE de áudio | 0.61 GB | [download](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/e5eb578a89295337b8ff433a035929ce0279e0b6/vae/minimax_h3_audio_vae_fp32.safetensors) | [página](https://huggingface.co/Comfy-Org/MiniMax-H3) |
| `loras/` | `minimax_h3_turbo_v4_step600_ema.safetensors` | LoRA Turbo v4-600 (Apache-2.0; herda as regras do H3) | 0.78 GB | [download](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora/resolve/43a74557ac3f6539db8e0f2a959d03feb7a81480/minimax_h3_turbo_v4_step600_ema.safetensors) | [página](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora) |

<details><summary>SHA-256</summary>

```
9255f52b6677845ad238f20dfaafa94727053694127ab7f255c048f0f9365779  models/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors
35a88d51044231fe332301d7a62aa81e3f2cba62febeb446e2c1e3e0ef76f2c6  models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
52a2c8c73583c86e4f41cdcce3a6ad0ea562987bc0bf3d60a0cef5f5c8e60c0e  models/vae/minimax_h3_video_vae_int8_convrot.safetensors
8e505d95dd1561d47abd43d4238fd40d9bb1ae9e147ed0a4cba778d76ae4db48  models/vae/minimax_h3_audio_vae_fp32.safetensors
5f3a626cd72c93a8b9318d6760c510bc5092d2ab13aaba1f932c5bab07a416d3  models/loras/minimax_h3_turbo_v4_step600_ema.safetensors
```

</details>

## Como usar

1. Igual ao workflow base; o modelo passa por **MiniMax-H3 Turbo LoRA** (força 1.0) e o `SamplerCustomAdvanced` recebe o **MiniMax-H3 Turbo Sampler**.
2. Steps no **BasicScheduler** (`simple`): 4 é o mínimo, 6–8 ficam visivelmente melhores; acima de 8 começa a dar nitidez exagerada.
3. `low_vram` desligado (bypass) é o mais nítido; ligado (merge) usa menos VRAM mas fica mais suave em bases INT8.

## Licença

Uso pessoal e comercial liberados até US$ 20 mi/ano de receita (acima disso, autorização da MiniMax). **Proibido nos EUA, UE, Reino Unido e Coreia do Sul, inclusive exibir ou distribuir as saídas lá (cláusula V.4)**: não use os vídeos em projetos publicados globalmente. Conteúdo publicado deve ser identificado como gerado por IA; proibido personificar pessoas reais sem consentimento; produto comercial deve exibir "MiniMax H3". LoRAs de terceiros herdam essas regras.

## Observações

- Comparado ao TaoMate 3 steps na mesma cena: 1008 s contra 524 s. Vale como alternativa de estética, não de velocidade.
- O autor avisa que, em 4 steps com movimento rápido, o v4 pode deixar rastro; 6–8 steps resolvem.
- O LoRA foi feito para T2V/I2V; aqui foi aplicado no Ref2VA e funcionou.
