import argparse
import torch
import logging
from PIL import Image
from torchvision import transforms as tfms
from tqdm.auto import tqdm
from transformers import CLIPTextModel, CLIPTokenizer
from diffusers import AutoencoderKL, UNet2DConditionModel, LMSDiscreteScheduler
import os
from tensorflow import keras

# Disable logging warnings
logging.disable(logging.WARNING)

def main(prompts, output_filename,neg_prompts=None,seed=None):
    # Initiating tokenizer and encoder
    tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14", torch_dtype=torch.float16)
    text_encoder = CLIPTextModel.from_pretrained("openai/clip-vit-large-patch14", torch_dtype=torch.float16).to("cuda")

    # Initiating the VAE
    vae = AutoencoderKL.from_pretrained("CompVis/stable-diffusion-v1-4", subfolder="vae", torch_dtype=torch.float16).to("cuda")

    # Initializing a scheduler and setting the number of sampling steps
    scheduler = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", num_train_timesteps=1000)
    scheduler.set_timesteps(50)

    # Initializing the U-Net model
    unet = UNet2DConditionModel.from_pretrained("CompVis/stable-diffusion-v1-4", subfolder="unet", torch_dtype=torch.float16).to("cuda")

    # Helper functions
    def load_image(p):
        return Image.open(p).convert('RGB').resize((512, 512))

    def pil_to_latents(image):
        init_image = tfms.ToTensor()(image).unsqueeze(0) * 2.0 - 1.0
        init_image = init_image.to(device="cuda", dtype=torch.float16)
        init_latent_dist = vae.encode(init_image).latent_dist.sample() * 0.18215
        return init_latent_dist

    def latents_to_pil(latents):
        latents = (1 / 0.18215) * latents
        with torch.no_grad():
            image = vae.decode(latents).sample
        image = (image / 2 + 0.5).clamp(0, 1)
        image = image.detach().cpu().permute(0, 2, 3, 1).numpy()
        images = (image * 255).round().astype("uint8")
        pil_images = [Image.fromarray(image) for image in images]
        return pil_images

    def text_enc(prompts, maxlen=None):
        if maxlen is None:
            maxlen = tokenizer.model_max_length
        inp = tokenizer(prompts, padding="max_length", max_length=maxlen, truncation=True, return_tensors="pt")
        return text_encoder(inp.input_ids.to("cuda"))[0].half()

    def prompt_2_img(prompts, neg_prompts=None, g=7.5, seed=100, steps=70, width=1280, height=720, save_int=False):
        bs = len(prompts)
        text = text_enc(prompts)
        if not neg_prompts:
            uncond = text_enc([""] * bs, text.shape[1])
        else:
            uncond = text_enc(neg_prompts, text.shape[1])
        emb = torch.cat([uncond, text])
        if seed:
            torch.manual_seed(seed)
        latents = torch.randn((bs, unet.in_channels, width // 8, height // 8), dtype=torch.float16)  # 변경된 부분
        scheduler.set_timesteps(steps)
        latents = latents.to("cuda").half() * scheduler.init_noise_sigma
        for i, ts in enumerate(tqdm(scheduler.timesteps)):
            inp = scheduler.scale_model_input(torch.cat([latents] * 2), ts)
            with torch.no_grad():
                u, t = unet(inp, ts, encoder_hidden_states=emb).sample.chunk(2)
            pred = u + g * (t - u)
            latents = scheduler.step(pred, ts, latents).prev_sample
            if save_int:
                if not os.path.exists(f'./steps'):
                    os.mkdir(f'./steps')
                latents_to_pil(latents)[0].resize((width, height)).save(f'steps/{i:04}.jpeg')  # 변경된 부분
        return latents_to_pil(latents)

    # Generating the image
    images = prompt_2_img(prompts=[prompts], neg_prompts=[neg_prompts], seed=[seed], steps=50)[0]
    images.save(output_filename)

if __name__ == "__main__":
    # You can specify the prompt and output filename here
    prompts = "Your text prompt here"
    neg_prompts='Your text negative prompt here'
    output_filename = "output.png"
    seed = "Your seed here"
    main(prompts, neg_prompts, output_filename, seed)