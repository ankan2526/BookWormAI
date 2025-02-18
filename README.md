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




## Backend Endpoints

- **/books**: Returns list of books
- **/books/search**: Returns list of books based on title
- **/llm/invoke**: Returns llm response based on the provided query
