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
    return result
