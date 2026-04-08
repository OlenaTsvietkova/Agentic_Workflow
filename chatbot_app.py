import streamlit as st
from haystack.dataclasses import ChatMessage
from haystack_integrations.components.generators.ollama import OllamaChatGenerator
from haystack.tools import ComponentTool
from haystack.components.agents import Agent
import os
from TavilyWebSearch import TavilyWebSearch

# ----------------------------
# 1️⃣ Initialize Tavily Component & Tool
# ----------------------------
tavily_component = TavilyWebSearch(api_key=os.getenv("TAVILY_API_KEY"))

web_tool = ComponentTool(
    name="web_search",
    description="Live web search via Tavily",
    component=tavily_component  # ✅ ComponentTool requires component=
)

# ----------------------------
# 2️⃣ Initialize Ollama Generator & Agent
# ----------------------------
model_name = "llama3.1"

chat_generator = OllamaChatGenerator(
    model=model_name,
    url="http://141.2.11.133:11434",
    timeout=30*60,
    generation_kwargs={
        "temperature": 0,
        "num_ctx": 8192
    },
    tools=[web_tool]
)

agent = Agent(
    chat_generator=chat_generator,
    tools=[web_tool]
)

# ----------------------------
# 3️⃣ Initialize Session State
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        ChatMessage.from_system(
            """
LLM is a helpful research assistant.
It uses web_search only when real-time or external information is needed.
"""
        )
    ]

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# ----------------------------
# 4️⃣ Chat Input
# ----------------------------
st.session_state.user_input = st.text_input("Type your request here:", st.session_state.user_input)

if st.button("Send") and st.session_state.user_input:
    user_text = st.session_state.user_input

    # Add user message
    st.session_state.messages.append(ChatMessage.from_user(user_text))

    # Run agent (calls Tavily if needed)
    resp = agent.run(messages=st.session_state.messages)

    # Extract assistant reply
    ai_reply = str(resp)
    st.session_state.messages.append(ChatMessage.from_assistant(ai_reply))

    # Clear input box
    st.session_state.user_input = ""

# ----------------------------
# 5️⃣ Display Conversation
# ----------------------------
for msg in st.session_state.messages:
    if msg.role == "user":
        st.markdown(f"**You:** {msg.text}")
    else:
        st.markdown(f"**AI:** {msg.text}")

# ----------------------------
# 6️⃣ Optional: Track which tools were invoked
# ----------------------------
def tools_used(run_output: dict) -> list[str]:
    seen, ordered = set(), []
    for msg in run_output.get("messages", []):
        if hasattr(msg, "tool_calls"):
            for call in msg.tool_calls:
                if call.tool_name not in seen:
                    ordered.append(call.tool_name)
                    seen.add(call.tool_name)
    return ordered

# Only display tools if last response exists
if "resp" in locals():
    st.markdown(f"**Tools invoked:** {tools_used(resp)}")