# Leveraging Catastrophic Forgetting to Develop Safe Diffusion Models against Malicious Finetuning

(NeurIPS 24) Leveraging Catastrophic Forgetting to Develop Safe Diffusion Models against Malicious Finetuning

## Environment Installation

Follow the instruction of installing diffusers and accelerate in the [diffusers](https://github.com/huggingface/diffusers) repository.

## Ckpt

Trained U-Net Ckpt will be released laterly.

## LT Train

``` python
bash train_latent.sh
```

## NG Train

``` python
bash train_noise.sh
```

## High Safety Train

``` python
bash train_high.sh
```

## Image Generation

``` python
python image_generation.py
```

## Dataset Format

Dataset example format is provided in datasets/metadata.jsonl. You need to use stable diffusion model or other models to generate images and save them in the same folder as the text file. Class 1 refers to clean images and class 2 refers to harmful images. You can use your own harmful and clean prompts with the same format to train the model.
