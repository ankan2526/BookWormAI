from langchain_google_genai import ChatGoogleGenerativeAI

class LLM_Helper:
    def __init__(self, model):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            # other params...
        )

    def invoke(self, prompt):
        try:
            return self.llm.invoke(prompt).content
        except Exception as e:
            return str(e)