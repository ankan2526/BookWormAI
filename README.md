# Books Website

A web application for searching books based on genre, viewing summaries, and interacting with an AI-powered chatbot for book-related queries.

## Features

- **Search Books**: Find books by genre.
- **View Summaries**: Get brief descriptions of books.
- **Chatbot Assistance**: Ask book-related questions using an AI chatbot.
- **User-Friendly UI**: Built with Angular or React for a smooth user experience.

## Tech Stack

- **Frontend**: Angular
- **Backend**: Python (FastAPI / Flask)
- **LLM**: Ollama models (llama3.2)
- **Langgraph**: To build agent with tools
- **Vector Database**: ChromaDB
- **Database**: SQLite

## Installation

### Prerequisites
- Node.js (for Angular)
- Python 3
- SQLite
- Ollama installed for running Llama 3 models

### Setup

#### Langsmith for tracing LLM Calls (Optional)
- Create a .env file in the /BookWormAI directory and add the below lines:
  ```text
  LANGSMITH_TRACING=true
  LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
  LANGSMITH_API_KEY="langsmith_api_key"
  LANGSMITH_PROJECT="BookWormAI"
  TAVILY_API_KEY="tavily_api_key"
  GOOGLE_API_KEY="google_api_key"
  ```
- Get your Langsmith API Key from [LangSmith](https://www.langchain.com/langsmith "Visit LangSmith's website") and place it in .env file in place of your_api_key.




## Backend Endpoints

- **/books**: Returns list of books
- **/books/search**: Returns list of books based on title
- **/llm/invoke**: Returns llm response based on the provided query
