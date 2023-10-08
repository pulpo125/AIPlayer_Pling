# https://github.com/divamgupta/stable-diffusion-tensorflow.git
# pip install git+https://github.com/divamgupta/stable-diffusion-tensorflow
# tensorflow==2.10.0
# h5py==3.7.0
# Pillow==9.2.0
# tqdm==4.64.1
# ftfy==6.1.1
# regex==2022.9.13
# tensorflow-addons==0.17.1

from tensorflow import keras
from stable_diffusion_tf.stable_diffusion import StableDiffusion
import argparse
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import cv2

parser = argparse.ArgumentParser()

parser.add_argument(
    "--prompt",
    type=str,
    nargs="?",
    default="a painting of a virus monster playing guitar",
    help="the prompt to render",
)

parser.add_argument(
    "--negative-prompt",
    type=str,
    help="the negative prompt to use (if any)",
)

parser.add_argument(
    "--output",
    type=str,
    nargs="?",
    default="output.png",
    help="where to save the output image",
)

parser.add_argument(
    "--H",
    type=int,
    default=512,
    help="image height, in pixels",
)

parser.add_argument(
    "--W",
    type=int,
    default=512,
    help="image width, in pixels",
)

parser.add_argument(
    "--scale",
    type=float,
    default=7.5,
    help="unconditional guidance scale: eps = eps(x, empty) + scale * (eps(x, cond) - eps(x, empty))",
)

parser.add_argument(
    "--steps", type=int, default=50, help="number of ddim sampling steps"
)

parser.add_argument(
    "--seed",
    type=int,
    help="optionally specify a seed integer for reproducible results",
)

parser.add_argument(
    "--mp",
    default=False,
    action="store_true",
    help="Enable mixed precision (fp16 computation)",
)

args = parser.parse_args()

if args.mp:
    print("Using mixed precision.")
    keras.mixed_precision.set_global_policy("mixed_float16")

generator = StableDiffusion(img_height=args.H, img_width=args.W, jit_compile=True)
img = generator.generate(
    args.prompt,
    negative_prompt=args.negative_prompt,
    num_steps=args.steps,
    unconditional_guidance_scale=args.scale,
    temperature=1,
    batch_size=1,
    seed=args.seed,
)
pnginfo = PngInfo()
pnginfo.add_text('prompt', args.prompt)
# Image.fromarray(img[0]).save(args.output, pnginfo=pnginfo)
resized_img = Image.fromarray(img[0]).resize((1280, 720))
resized_img.save(args.output, pnginfo=pnginfo)
print(f"saved at {args.output}")