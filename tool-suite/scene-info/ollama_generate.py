import ollama
import json

def generate_text(prompt, system_prompt=None, model="llava", image_path=None):
    args = {
        "prompt": prompt,
        "model": model,
        "stream": False,
    }
    if system_prompt:
        args["system"] = system_prompt
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

YOU DON'T HAVE ACCESS TO THE IMAGE. Generate the questions that helps with the objective if some human answered
these questions by looking at the image.

Your job is to generate a list of intermediate questions such that the answers to those questions will help us answer the
question in the objective. Output the list as a JSON.
"""

GEN_QUESTIONS_PROMPT= """
{GEN_QUESTIONS_SYS_PROMPT}

Objective: {prompt}
"""

GEN_QUESTIONS_SYS_PROMPT = """
You are given an image and a set of questions. The questions are in a JSON list. Answer each question and return a list of dictionaries.

Example input format:
[
"Question 1",
"Question 2",
"Question3"
]

Example output format:
[
{"question":"Question 1", "answer": "Answer 1"},
{"question":"Question 2", "answer": "Answer 2"},
{"question":"Question 3", "answer": "Answer 3"},
]
"""

GEN_QUESTIONS_PROMPT_TEMPLATE = """
Answer the following questions about the image and return a json output of questions and answers.
{questions}
"""


def generate_questions(prompt, image_path=None, model="llava"):
    return generate_text(
        prompt=prompt, image_path=image_path, system_prompt=GEN_QUESTIONS_SYS_PROMPT, model=model
    )


def answer_questions(questions, image_path, model="llava"):
    prompt = GEN_QUESTIONS_PROMPT_TEMPLATE.format(json.dumps(questions))
    return generate_text(
        prompt=prompt, image_path=image_path, system_prompt=GEN_QUESTIONS_SYS_PROMPT, model=model
    )
