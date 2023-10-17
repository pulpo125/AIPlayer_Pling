import time
from tensorflow import keras
import matplotlib.pyplot as plt
import cv2
import keras_cv
import argparse

def main(prompt, output_filename):
        
    model = keras_cv.models.StableDiffusion(img_width=512, img_height=512) #모델에 입력될 크기
    images = model.text_to_image(prompt, batch_size=1) # prompt
    
    # 이미지 출력 함수 
    def plot_image(images, figsize=(12.8, 7.2), width=1280, height=720):
        plt.figure(figsize=figsize)
        plt.imshow(images, extent=[0, width, 0, height])
        plt.axis("off")
        plt.show()

    # 같은 경로에 이미지 저장하는 함수
    
    def save_image(images, output_filename, width=1280, height=720):
        path = './'
        # 이미지 크기를 지정된 width와 height로 조정
        resized_image = cv2.resize(images, (width, height))
        cv2.imwrite(path + output_filename, resized_image)

    plot_image(images[0])  # Display the image
    save_image(images[0], output_filename)  # Save the image to the same directory

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and save images from text prompts.")
    parser.add_argument("prompt", type=str, help="Text prompt for image generation")
    parser.add_argument("output_filename", type=str, help="Filename for the generated image")

    args = parser.parse_args()
    main(args.prompt, args.output_filename)