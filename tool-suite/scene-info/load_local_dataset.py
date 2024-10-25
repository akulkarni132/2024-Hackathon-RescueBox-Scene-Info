import os
from pathlib import Path
from ollama_generate import generate_text

def load_local_dataset(file_path):
    text_data = list()
    labels_data = list()
    file_paths = list()

    curr_label = 0
    labels = []

    for item in os.listdir(file_path):
        if os.path.isdir(Path(file_path, item)):
            labels.append(item)

            nested_files = os.listdir(Path(file_path, item))
            for file in nested_files:
                file_path = os.path.join(Path(file_path, item), file)
                file_paths.append(file_path)
                text_data.append(item)
                labels_data.append(curr_label)
        curr_label += 1

    return text_data, labels_data, file_paths

if __name__ == "__main__":
    # Load dataset
    abs_path = os.environ['USER']
    text_data, labels_data, file_paths = load_local_dataset(abs_path)

    # Try it on one image
    img = {'file_path': file_paths[0], 'class_name': text_data[0], 'class_number': labels_data[0]}

    prompt = "{'prompt': 'Does the following image contain people? Format your response as a Python dictionary with a prediction key and a facts key', 'facts':[]}"
    system_prompt = "You are provided with a JSON object containing two keys: 'prompt' and 'facts'. Your task is to complete the value of 'facts' by breaking down the 'prompt' logically and providing clear, step-by-step reasoning which you will append to the 'facts' value. This reasoning should be a detailed explanation of the underlying concepts, context, or connections needed to fully understand and respond to the 'prompt'. Think about what other questions you could ask yourself to better inform your prediction. You will output your response to the prompt as a JSON object in the format of {'prediction': 'your yes or no answer', 'facts':['your', 'reasoning', 'here']}."

    result = generate_text(prompt, img['file_path'], system_prompt)
    print(result)