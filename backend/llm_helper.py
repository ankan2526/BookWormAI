from langchain_community.llms import Ollama

class LLM_Helper:
    def __init__(self, model):
        self.llm = Ollama(model=model)

    def invoke(self, prompt):
        return self.llm.invoke(prompt)