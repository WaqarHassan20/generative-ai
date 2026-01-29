from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    messages: Annotated[list, add_messages]
    # I want an annotated list of messages which must annotate with add_messages


graph_builder = StateGraph(State)

# Hey state graph, this is my schema for the state
# Please give me the graph builder for this state


def chatbot(state: State):
    print("\n\nInside the chatbot node!", state)
    return {"messages": ["Hi, this is a message from the chatbot!"]}


def sampleNode(state: State):
    print("\n\nInside the sampleNode node!", state)
    return {"messages": ["This is a sample node message."]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("sampleNode", sampleNode)

graph_builder.add_edge(start_key=START, end_key="chatbot")
graph_builder.add_edge(start_key="chatbot", end_key="sampleNode")
graph_builder.add_edge(start_key="sampleNode", end_key=END)

graph = graph_builder.compile()

updated_graph = graph.invoke(State(messages=["Hi! My name is Waqar UL Hassan."]))

print("\n\nUpdated Graph : ", updated_graph)

# state = {"messages": ["Hi there"]}
# node runs: chatbot(state: ["Hey there"]) -> {"message": ["Hi, this is a message from the chatbot!"]}
# state = {"messages": ["Hi there"," Hi, this is a message from the chatbot!"]}

# ================================================================================================== #

# Note to read and understand:

# LangGraph works like a state machine for AI logic. The State defines shared memory
# (here, a messages list). Each node is a pure function that reads the current state
# and returns partial updates instead of mutating state directly. The Annotated[list,
# add_messages] tells LangGraph to APPEND new messages to the existing list rather than
# overwrite it. LangGraph then merges these updates automatically and passes the
# updated state to the next node based on graph edges, making it ideal for building
# multi-step, branching, or agent-style workflows in Generative AI.
