# from groq import Groq
import streamlit as st

# from importnb import Notebook

# with Notebook():
#     import rag

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

# img = st.image("./icon.png")
st.logo("./icon.png", size="large")

if "messages" not in st.session_state:
    st.session_state["messages"] = []
if len(st.session_state.messages) == 0:
    st.markdown("## How can I help you?")

if len(st.session_state.messages) != 0:
    for msg in st.session_state.messages:
     if msg["role"]=="assistant": 
        st.chat_message(msg["role"], avatar="./icon.png").write(msg["content"])
     else :
        st.chat_message(msg["role"],avatar=":material/person:").write(msg["content"])
     
if prompt := st.chat_input("Enter your message"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message(name= "person",avatar=":material/person:").write(prompt)

    # config = {"configurable": {"thread_id": "7896323"}}
    # answer = rag.langgraph_agent_executor.invoke(
    #     {"messages": [("user", prompt)]},
    #     config,
    # )["messages"][-1]

    # msg = answer.content

    st.session_state.messages.append({"role": "assistant", "content": "echo " + prompt})
    st.chat_message(name="squarest", avatar="./icon.png").write("echo " + prompt)
st.write("Hello I am not a accurrate information provider")