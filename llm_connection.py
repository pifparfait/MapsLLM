import ollama

class LLM_executor:
    def __init__(self):
        pass

    def get_answer(self, prompt):
        response = ollama.generate(model='qwen2.5:0.5b', prompt = prompt + '. Give a short answer, and do it directly.')
        return response['response']