import os
os.environ['CUDA_VISIBLE_DEVICES'] = '2'
import torch
from tqdm import tqdm
import random
import json
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler, DiffusionPipeline,StableDiffusionXLPipeline

model_paths="model_path"
output_paths="outputs_path"
image_class=2 #1

pipeline = DiffusionPipeline.from_pretrained(
                model_paths,
                torch_dtype=torch.float16,
                safety_checker=None
           )
pipeline.set_progress_bar_config(disable=True)

pipe = pipeline.to("cuda")

prompts=[]
jsonl=[]
with open(f"/data1/panjiadong/project/make_regret/class{image_class}_text_splited.jsonl","r") as f:
    for line in f:
        jsonl.append(json.loads(line))
for i in range(100):
    prompts.append(jsonl[i]["text"])

image_dir = "images"
if not os.path.exists(output_paths):
    os.makedirs(output_paths)
for i in tqdm(range(100)):
    prompt=prompts[i]
    image = pipe(prompt,guidance_scale=7.5).images[0]  
    image.save(f"{output_paths}/class_{image_class}_{i}.jpg")