import os
os.environ['TF_ENABLE_ONEDNN_OPTS']='0'
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

from googletrans import Translator
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import cv2
from tensorflow import keras
from stable_diffusion_tf.stable_diffusion import StableDiffusion

path = os.getcwd()
output = path + "\\main\\static\\result\\result_img.png"


# 플레이리스트 타이틀 번역 및 전처리
def title2prompt(new_title):
    translator=Translator()
    new_title_trans=translator.translate(new_title,dest='en').text
    prompt_str = 'photograph, ' + new_title_trans + ', landscape, 8k uhd'
    return prompt_str

# 이미지 생성
keras.mixed_precision.set_global_policy("mixed_float16")
generator = StableDiffusion(img_height=512, img_width=512, jit_compile=True)

def generateImg(prompt_str):
    img = generator.generate(
        prompt=prompt_str,
        negative_prompt="fingers, toe, body, hair, face, eyes, nose, ears, lip, legs, arms, hands, feet, girl, boy, people",
        num_steps=50,
        unconditional_guidance_scale=7.5,
        temperature=1,
        batch_size=1,
        seed=123,
    )
    pnginfo = PngInfo()
    pnginfo.add_text('prompt', prompt_str)
    resized_img = Image.fromarray(img[0]).resize((1280, 720))
    resized_img.save(output, pnginfo=pnginfo)
    print(f"saved at img")