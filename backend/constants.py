MODEL = "gemini-1.5-flash"
DB_PATH = r"/Users/ankanmahapatra/Desktop/genAI/BookWormAI/backend/books.db"
DB_URI = "sqlite:///books.db"
LIMIT_ROWS = 10

TEXT_TO_SQL_PROMPT = """
Given an user query, create a syntactically correct {dialect} query that can be executed on the database.
Unless the user specifies in their query a specific number of rows they wish to obtain, always limit the number of rows returned to {LIMIT_ROWS}.

Never query for all the colums from a specific table. Only ask for a few columns that are relevant to the user query.

Pay attention to the user query and try to understand what they are asking for. If the user query is ambiguous, ask for clarification.

Only use the following tables:
{table_info}

Query: {query}

Note: Only allow read operations on the database. Do not allow any write operations.
"""