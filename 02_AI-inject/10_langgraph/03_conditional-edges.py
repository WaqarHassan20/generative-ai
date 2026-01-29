from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from typing import Optional, Literal
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]


# Its like the first node which initializes the state


def chatbot(state: State) -> State:
    print("\n\Chatbot node!", state)
    response = client.chat.completions.create(
        model="gemini-2.5-flash-lite",
        messages=[{"role": "user", "content": state.get("user_query")}],
    )
    state["llm_output"] = response.choices[0].message.content
    return state


# so you get a state and manipulate it and then return it back as new state
# Its like the first node which initializes the state


def chatbot_gemini(state: State) -> State:
    print("\n\nChatbot_gemini node!", state)
    response = client.chat.completions.create(
        model="gemini-2.5-flash-lite",
        messages=[{"role": "user", "content": state.get("user_query")}],
    )
    state["llm_output"] = response.choices[0].message.content
    return state


def evaluate_response(state: State) -> Literal["chatbot_gemini", "end_node"]:
    if True:
        return "end_node"
    return "chatbot_gemini"


def end_node(state: State) -> State:
    print("\n\nEnd node!", state)
    print("\n\nFinal State Reached:")
    return state


graph_builder = StateGraph(state_schema=State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("chatbot_gemini", chatbot_gemini)
graph_builder.add_node("end_node", end_node)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response)
graph_builder.add_edge("chatbot_gemini", "end_node")
graph_builder.add_edge("end_node", END)

graph = graph_builder.compile()
updated_state = graph.invoke(
    # State({"user_query": "Explain LangGraph in simple words."})
    State({"user_query": "what is 5 - 1 + 2 + 10 / 2 ?"})
)
print("\n\nUpdated State : ", updated_state)


# # My final output which i get :
# Final State Reached: {'user_query': 'Explain LangGraph in simple words.', 'llm_output': 'Imagine you have a bunch of different tools or skills you can use to solve a problem. LangGraph is like a smart system that helps you **organize and chain these tools together in a flexible and interactive way to achieve a goal.**\n\nHere\'s a breakdown using a simple analogy:\n\n**Think of it like building a Rube Goldberg machine:**\n\n*   **The Goal:** Your Rube Goldberg machine has a specific goal, like ringing a bell.\n*   **The Tools/Steps:** Each part of the machine is a "tool" or a "step" that performs a specific action. For example:\n    *   A marble rolling down a ramp.\n    *   A lever that flips a switch.\n    *   A fan that blows a balloon.\n    *   A falling weight that hits a button.\n*   **The Flow/Logic:** The magic is in *how* these steps are connected and *when* they happen. The marble rolling down the ramp *triggers* the lever, which *triggers* the fan, and so on.\n\n**How LangGraph relates to this:**\n\n1.  **Nodes (The Tools/Steps):** In LangGraph, each "node" represents a specific task or action. These could be:\n    *   **Calling an AI model:** Asking a language model to write something, summarize, or answer a question.\n    *   **Accessing a database:** Fetching information.\n    *   **Running a piece of code:** Performing a calculation.\n    *   **Asking a user for input:** Getting more information.\n\n2.  **Edges (The Connections/Logic):** The "edges" are the pathways that connect these nodes. They define the flow of execution – what happens next based on the outcome of the previous node. This is where the "smart" part comes in. LangGraph allows for:\n    *   **Conditional branching:** If the AI model gives a certain answer, go down this path. If it gives another answer, go down a different path. (Like a fork in the road).\n    *   **Looping:** If more information is needed, go back to a previous step. (Like a circular path).\n    *   **Parallel execution:** If two tasks can happen independently, do them at the same time.\n\n3.  **The "Graph":** All these nodes and edges together form a "graph." It\'s a visual representation of the entire workflow.\n\n**Why is it "Graph" and not just a list?**\n\nBecause traditional linear programs (like a simple list of instructions) can\'t handle complex decision-making or iterative processes easily. A graph allows for much more intricate and dynamic workflows.\n\n**What makes it "Lang" (Language)?**\n\nLangGraph is particularly good at orchestrating **large language models (LLMs)**. This means it\'s designed to help you build applications that use LLMs in sophisticated ways, where the LLM\'s output might determine the next step in the process.\n\n**In simpler terms, LangGraph helps you:**\n\n*   **Break down complex tasks into smaller, manageable steps.**\n*   **Decide intelligently which step to take next.**\n*   **Create dynamic and interactive workflows.**\n*   **Build sophisticated AI applications that can reason, adapt, and learn.**\n\n**Think of it as building an intelligent agent that can:**\n\n*   **"Think":** Process information and make decisions.\n*   **"Act":** Use tools and execute actions.\n*   **"Learn":** Potentially adjust its behavior based on feedback or outcomes.\n\nSo, if you want to build something like an AI that can browse the web, analyze data, write reports, and then iterate on those reports based on feedback, LangGraph is the tool that helps you connect all those pieces into a coherent and intelligent system.'}


# Updated State :  {'user_query': 'Explain LangGraph in simple words.', 'llm_output': 'Imagine you have a bunch of different tools or skills you can use to solve a problem. LangGraph is like a smart system that helps you **organize and chain these tools together in a flexible and interactive way to achieve a goal.**\n\nHere\'s a breakdown using a simple analogy:\n\n**Think of it like building a Rube Goldberg machine:**\n\n*   **The Goal:** Your Rube Goldberg machine has a specific goal, like ringing a bell.\n*   **The Tools/Steps:** Each part of the machine is a "tool" or a "step" that performs a specific action. For example:\n    *   A marble rolling down a ramp.\n    *   A lever that flips a switch.\n    *   A fan that blows a balloon.\n    *   A falling weight that hits a button.\n*   **The Flow/Logic:** The magic is in *how* these steps are connected and *when* they happen. The marble rolling down the ramp *triggers* the lever, which *triggers* the fan, and so on.\n\n**How LangGraph relates to this:**\n\n1.  **Nodes (The Tools/Steps):** In LangGraph, each "node" represents a specific task or action. These could be:\n    *   **Calling an AI model:** Asking a language model to write something, summarize, or answer a question.\n    *   **Accessing a database:** Fetching information.\n    *   **Running a piece of code:** Performing a calculation.\n    *   **Asking a user for input:** Getting more information.\n\n2.  **Edges (The Connections/Logic):** The "edges" are the pathways that connect these nodes. They define the flow of execution – what happens next based on the outcome of the previous node. This is where the "smart" part comes in. LangGraph allows for:\n    *   **Conditional branching:** If the AI model gives a certain answer, go down this path. If it gives another answer, go down a different path. (Like a fork in the road).\n    *   **Looping:** If more information is needed, go back to a previous step. (Like a circular path).\n    *   **Parallel execution:** If two tasks can happen independently, do them at the same time.\n\n3.  **The "Graph":** All these nodes and edges together form a "graph." It\'s a visual representation of the entire workflow.\n\n**Why is it "Graph" and not just a list?**\n\nBecause traditional linear programs (like a simple list of instructions) can\'t handle complex decision-making or iterative processes easily. A graph allows for much more intricate and dynamic workflows.\n\n**What makes it "Lang" (Language)?**\n\nLangGraph is particularly good at orchestrating **large language models (LLMs)**. This means it\'s designed to help you build applications that use LLMs in sophisticated ways, where the LLM\'s output might determine the next step in the process.\n\n**In simpler terms, LangGraph helps you:**\n\n*   **Break down complex tasks into smaller, manageable steps.**\n*   **Decide intelligently which step to take next.**\n*   **Create dynamic and interactive workflows.**\n*   **Build sophisticated AI applications that can reason, adapt, and learn.**\n\n**Think of it as building an intelligent agent that can:**\n\n*   **"Think":** Process information and make decisions.\n*   **"Act":** Use tools and execute actions.\n*   **"Learn":** Potentially adjust its behavior based on feedback or outcomes.\n\nSo, if you want to build something like an AI that can browse the web, analyze data, write reports, and then iterate on those reports based on feedback, LangGraph is the tool that helps you connect all those pieces into a coherent and intelligent system.'}
