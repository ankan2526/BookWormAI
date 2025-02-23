from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import START, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from langgraph.checkpoint.memory import MemorySaver

import sqlite3
from typing import List
from langchain_community.utilities import SQLDatabase
from langchain_community.tools import TavilySearchResults
from constants import DB_PATH, DB_URI, LIMIT_ROWS, TEXT_TO_SQL_PROMPT, MODEL

from dotenv import load_dotenv

load_dotenv()

db = SQLDatabase.from_uri(DB_URI)
dialect = db.dialect
table_info = db.get_table_info()

## These are tools that will be used by AI Agent to make decisions and answer questions
def get_text_to_sqlite_prompt(query: str) -> str:
    """This function will return a text to sqlite prompt

    Args:
        query (str): The query to be converted to sqlite

    Returns:
        str: The text to sqlite prompt
    """
    text_to_sqlite_prompt = TEXT_TO_SQL_PROMPT.format(dialect=dialect, LIMIT_ROWS=LIMIT_ROWS, table_info=table_info, query=query)
    return text_to_sqlite_prompt



def execute_sqlite_query(query: str) -> List:
    """This function will execute a sqlite query

    Args:
        query (str): The sqlite query to be executed

    Returns:
        List: The result of the query
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result



def search_tool(query: str) -> List:
    """This function will search results from web

    Args:
        query (str): The query to be searched

    Returns:
        List: The search results
    """
    tool = TavilySearchResults(
        max_results=5,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=True,
        include_images=True,
        # include_domains=[...],
        # exclude_domains=[...],
        # name="...",            # overwrite default tool name
        # description="...",     # overwrite default tool description
        # args_schema=...,       # overwrite default args_schema: BaseModel
    )
    result = tool.invoke(query)
    return result





llm = ChatGoogleGenerativeAI(
    model=MODEL,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
tools = [get_text_to_sqlite_prompt, execute_sqlite_query, search_tool]
llm_with_tools = llm.bind_tools(tools)

sys_msg = SystemMessage(content="""You are an AI agent that helps readers answer book related queries.
                        You have access to a database of books and you can search the web for additional information.""")

def assistant(state: MessagesState):
    return {"messages": [llm.invoke([sys_msg] + state["messages"])]}

builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")

memory = MemorySaver()
react_graph_memory = builder.compile(checkpointer=memory)

def invoke(query, thread_id):
    config = {"thread_id": thread_id}
    messages = react_graph_memory.invoke({"messages": [HumanMessage(content=query)]}, config=config)
    result = messages["messages"][-1].content
    return {"query": query, "result": result}