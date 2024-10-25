import ollama

def generate_text(instruction, file_path, system_prompt, model='llava'):
    result = ollama.generate(
        model=model,
        prompt=instruction,
        system=system_prompt,
        images=[file_path],
        stream=False
    )['response']
    return result
