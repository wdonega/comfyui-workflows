# ACE-Step 1.5 Turbo · música

[comfyui-workflows](../../README_ptBR.md) › **ACE-Step 1.5 Turbo · música**

O template oficial `audio_ace_step_1_5_split` (modelo turbo + dois text encoders Qwen + VAE). Gera música com vocal a partir de tags de estilo e letra, em 8 steps. Licença MIT: a opção livre para trilhas de projetos publicados.

| | |
|---|---|
| Status | ✅ testado |
| Família | ACE-Step 1.5 |
| Licença | [MIT](https://opensource.org/license/mit) |
| Download total | 10.03 GB |
| Teste | exemplo do template (K-pop com letra) encurtado para 30 s |
| Tempo | **16s** (RTX 5060 Ti 16 GB, 2026-10-22) |
| Pico de VRAM | 11267 MiB |

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

## Modelos

| Pasta (`models/…`) | Arquivo | Papel | Tamanho | Download | Página |
|---|---|---|---|---|---|
| `diffusion_models/` | `acestep_v1.5_turbo.safetensors` | ACE-Step 1.5 Turbo | 4.79 GB | [download](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/6707deb277e9e0907fd9c14ce6b6f1d695c6a3fc/split_files/diffusion_models/acestep_v1.5_turbo.safetensors) | [página](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files) |
| `text_encoders/` | `qwen_0.6b_ace15.safetensors` | text encoder Qwen 0.6B | 1.19 GB | [download](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/6707deb277e9e0907fd9c14ce6b6f1d695c6a3fc/split_files/text_encoders/qwen_0.6b_ace15.safetensors) | [página](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files) |
| `text_encoders/` | `qwen_1.7b_ace15.safetensors` | text encoder Qwen 1.7B (letra) | 3.71 GB | [download](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/6707deb277e9e0907fd9c14ce6b6f1d695c6a3fc/split_files/text_encoders/qwen_1.7b_ace15.safetensors) | [página](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files) |
| `vae/` | `ace_1.5_vae.safetensors` | VAE de áudio | 0.34 GB | [download](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/6707deb277e9e0907fd9c14ce6b6f1d695c6a3fc/split_files/vae/ace_1.5_vae.safetensors) | [página](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files) |

<details><summary>SHA-256</summary>

```
3f6e0797fad420a39bd33979eb6e840e30989e34a3794e843d23b60ec6e422d7  models/diffusion_models/acestep_v1.5_turbo.safetensors
fd4590c82153b8ddb67e15a2e7aaa8afa8b83a858c8a9b82a4831063156aa7a7  models/text_encoders/qwen_0.6b_ace15.safetensors
ed63e9247d1f55f3ace04fa11e95b085fc82d459c82c5626f0b2e37b91ebd710  models/text_encoders/qwen_1.7b_ace15.safetensors
6de92e3a862acd287e08b024ac90f0783a8635451b728721a33ff03565bcb2bb  models/vae/ace_1.5_vae.safetensors
```

</details>

## Como usar

No **TextEncodeAceStepAudio1.5**: tags de estilo e a letra com seções. Duração em segundos no **EmptyAceStep1.5LatentAudio** (120 no template). Há variantes XL (4B) nos templates do ComfyUI, que pedem ≥ 12 GB com offload.

## Licença

MIT: uso pessoal e comercial livres, sem limite; basta manter o aviso de copyright ao redistribuir os pesos.

## Observações

- Muito rápido: 30 s de música em 16 s.
