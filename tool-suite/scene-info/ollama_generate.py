import ollama
import os
from pathlib import Path
import imghdr
from PIL import Image

def generate_text(instruction, file_path, system_prompt):
    result = ollama.generate(
        model='llava',
        prompt=instruction,
        system=system_prompt,
        images=[file_path],
        stream=False
    )['response']
    img=Image.open(file_path, mode='r')
    img = img.resize([int(i/1.2) for i in img.size])
    # display(img) 
    # for i in result.split('.'):
        # print(i, end='', flush=True)
    return result