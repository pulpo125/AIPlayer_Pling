import argparse
from kerascv_stableDiffusion import main

parser = argparse.ArgumentParser()

parser.add_argument(
    "--prompt", # 텍스트 입력
    type=str,
    nargs="?",
    default="beach,photograph,landscape, simple",
    help="the prompt to render",
)

parser.add_argument( 
    "--output", # 사진
    type=str,
    nargs="?",
    default="output.png",
    help="where to save the output image",
)


args = parser.parse_args()

main(prompt=args.prompt, output_filename=args.output)
print(f"saved at {args.output}")