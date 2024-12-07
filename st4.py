# from groq import Groq
import streamlit as st
from importnb import Notebook

with Notebook():
    import rag

# st.set_page_config(layout="wide")
# Custom CSS to center the title
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
         margin-top: -60px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown("<h2 class='centered-title'>squarestAI</h2>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


st.logo("./icon.png", size="large")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
       
    ]
if (len(st.session_state.messages)==0):
    st.markdown("## How can I help you?")



for msg in st.session_state.messages:
       st.chat_message(msg["role"]).write(msg["content"])
if prompt:=st.chat_input("Enter your Message"):
   

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    st.chat_message("user").write(prompt)

    config = {"configurable": {"thread_id": "7896323"}}
    answer = rag.langgraph_agent_executor.invoke(
        {"messages": [("user", prompt)]},
        config,
    )["messages"][-1]

    msg = answer.content

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
