import argparse
from pytorch_stableDiffusion import main

parser = argparse.ArgumentParser()

parser.add_argument(
    "--prompts",
    type=str,
    nargs="?",
    default="[beach,photograph,landscape, simple]",
    help="the prompt to render",
)

parser.add_argument(
    "--negative-prompts",
    type=str,
    default="fingers, toe,body, hair, face, eyes, nose, ears, lip, legs, arms, hands, feet, girl, boy, people",
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
    "--seed",
    type=int,
    default=100,
    help="seed",
)

args = parser.parse_args()

main(prompts=args.prompts, output_filename=args.output, neg_prompts=args.neg_prompts, seed=args.seed)
print(f"saved at {args.output}")