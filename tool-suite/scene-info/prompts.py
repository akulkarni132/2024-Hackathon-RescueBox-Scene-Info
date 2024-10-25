# Function that feeds LLM text prompt and image and generate output

import ollama_generate as og

text_prompt = "Where is this image located? Are there any people in this image? If so, describe them. Is this image indoors or outdoors? Where is the image located? Is there any text in this image? If so, what does it say and what does that signify? Are there any unique identifying features?"
# image_path = "/Users/akulkarni/Documents/Handpicked Images/explosive_0537.jpg"
# output=og.generate_text(prompt=text_prompt, image_path=image_path)
# print(type(output))

import os
import pandas as pd

# df = pd.DataFrame(columns=["Image", "Output"])

folder_path = "/Users/akulkarni/Documents/Handpicked Images 2"

def analyze_images(folder_path):
    result_dict = {"Image": [], "Output": []}
    image_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            filepath = os.path.join(folder_path, filename)
            output=og.generate_text(prompt=text_prompt, image_path=filepath)
            result_dict["Image"].append(filepath)
            result_dict["Output"].append(output)
            print(filename)
    df = pd.DataFrame(result_dict)
    return df

df = analyze_images(folder_path)
output_filepath = "tool-suite/scene-info/output2.csv"
df.to_csv(output_filepath)