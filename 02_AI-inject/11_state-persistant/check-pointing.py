from langgraph.checkpoint.mongodb import MongoDBSaver
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from typing import Annotated
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("GEMINI_API_KEY"))


# yeh init chat model Ali Abbas Chadhar ki repo say naqal shuda hai
llm = init_chat_model(
    model="gemini-2.5-flash-lite",
    model_provider="google_genai",
    api_key=os.environ.get("GEMINI_API_KEY"),
)


class State(TypedDict):
    messages: Annotated[list, add_messages]
    # I want an annotated list of messages which must annotate with add_messages


graph_builder = StateGraph(State)

# Hey state graph, this is my schema for the state
# Please give me the graph builder for this state


def chatbot(state: State):
    print("\n\nInside the chatbot node!", state)
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}


graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(start_key=START, end_key="chatbot")
graph_builder.add_edge(start_key="chatbot", end_key=END)

graph = graph_builder.compile()

def compile_graph_with_check_pointer(check_pointer):
    graph_with_check_pointer = graph_builder.compile(checkpointer=check_pointer)
    return graph_with_check_pointer

DB_URL = os.getenv("DB_URL")
print("DB_URL:", DB_URL)

with MongoDBSaver.from_conn_string(DB_URL) as check_pointer:
    graph_with_check_pointer = compile_graph_with_check_pointer(
        check_pointer=check_pointer
    )
    config = {"configurable": {"thread_id": "waqarhassan"}}

    
    # print(graph.get_graph().draw_ascii())
    # print(graph.get_graph().draw_mermaid())

    for chunk in graph_with_check_pointer.stream(
        # State({"messages": ["My name is Waqar Hassan. Tell me a joke about my name"]}),
        State({"messages": "what is my name ? Tell me about the joke you told me earlier about me."}),
        config=config,
        stream_mode="values",
    ):
        chunk["messages"][-1].pretty_print()

    # print(chunk)