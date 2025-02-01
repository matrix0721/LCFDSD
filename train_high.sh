CUDA_VISIBLE_DEVICES=7 accelerate launch --mixed_precision="bf16" --multi_gpu  train_test.py \
  --pretrained_model_name_or_path model/stable-diffusion-v1-4 \
  --output_dir outputs\
  --resolution=768 --center_crop --random_flip \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --gradient_checkpointing \
  --max_train_steps=10000 \
  --learning_rate=1e-5 \
  --max_grad_norm=1 \
  --lr_scheduler="cosine" --lr_warmup_steps=0 \
  --checkpointing_steps 1000 \
  --num_train_epochs 5\
  --mixed_precision bf16 \
  --checkpoints_total_limit 3\
  --l 0.0 \
  --lambda_total 0.00005 \
  --lambda_contrast 1.0 \
  --report_to "wandb" \
  #--use_ema \
