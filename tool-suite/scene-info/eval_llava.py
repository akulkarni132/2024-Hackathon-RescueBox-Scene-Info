from ollama_generate import generate_text
import pandas as pd
import argparse
from tqdm import tqdm
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--prompt', type=str, help='Prompt to generate text for', required=True)
parser.add_argument('--input_dir', type=str, help='Directory containing the input images', default='Handpicked Images')
parser.add_argument('--n', type=int, help='Number of rows to generate text for', default=None)
parser.add_argument('--output', type=str, help='Output file to save the generated text', default='output.csv')
args = parser.parse_args()

input_dir = Path(args.input_dir)

PROMPT = args.prompt
df = pd.read_csv('indoor_output_input.csv')
n = args.n if args.n else df.shape[0]
df = df[:n]

images = df.image_filename

res = []
for image in tqdm(images):
    llava_res = generate_text(PROMPT, image_path=str(input_dir/image))
    print(llava_res)
    res.append(llava_res)

df["res"] = res

df.to_csv(args.output, index=False)