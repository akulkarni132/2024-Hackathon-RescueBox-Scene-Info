import ollama


def generate_text(prompt, system_prompt, model="llava", image_path=None):
    args = {
        "prompt": prompt,
        "system": system_prompt,
        "model": model,
        "stream": False,
    }
    if image_path:
        args["images"] = [image_path]
    print(args)
    result = ollama.generate(**args)["response"]
    return result


# Chain of thought generation:
#   n-1 steps of "gather_knowledge" followed by "answer_question"
#
# gather_knowledge:
#   generate_questions
#   answer_questions
"""
Facts: 
{
   "Prompt": "question"
}
[
{"question": "Question 1", "answer": "answer1"},
{"question": "Question 2", "answer": "answer2"},
...
{"question": "Question n", "answer": "answern"}
]

"""

GEN_QUESTIONS_SYS_PROMPT = """
You are given a prompt and an objective. The objective is generally a question that we want answered about the image.
Your job is to generate a list of intermediate questions such that the answers to those questions will help us answer the
question in the objective. Output the list as a JSON.
"""


def generate_questions(prompt, image_path=None, model="llava"):
    return generate_text(
        prompt=prompt, image_path=image_path, system_prompt=GEN_QUESTIONS_SYS_PROMPT, model=model
    )


response = generate_questions("Is this image taken indoors or outdoors?", image_path="car-image.jpg")
print(response)
