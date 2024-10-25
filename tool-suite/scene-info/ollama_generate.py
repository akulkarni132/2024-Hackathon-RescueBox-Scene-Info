import ollama

def generate_text(prompt, system_prompt, model='llava', image_path=None):
    args = {
        "prompt": prompt,
        "system": system_prompt,
        "model": model,
        "stream": False,
    }
    if image_path:
        args["images"] = [image_path]
    
    result = ollama.generate(**args)['response']
    return result
