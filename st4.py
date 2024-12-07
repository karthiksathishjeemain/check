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
    st.markdown("#### How can I help you?")

# def clear_input():

#     st.session_state.user_input = st.session_state.input_text
#     st.session_state.input_text = ""


# def Answer_queries():
#     st.session_state.input_text = "Tell Me"


# def Get_SHIELD_report():
#     st.session_state.input_text = "Get me SHIELD report for <project name>"


# def Book_site_visit():
#     st.session_state.input_text = "Book a site visit for me for <project name> on <date>. My contact details are: <Name>, <Mobile No.>"


# def Home_loan_sanction():
#     st.session_state.input_text = "I'd like to apply for home loan sanction. Here are my PAN, latest IT return and salary slip. My contact details are: <Name>, <Mobile No.>"

# placeholder = st.empty()
# if len(st.session_state.messages) > 0:
#     container = st.container(height=400,border=False)
#     for msg in st.session_state.messages:
#         container.chat_message(msg["role"]).write(msg["content"])

# elif(len(st.session_state.messages)==0):
     
#      st.markdown("## How can I help you?")
    #  st.markdown("### How can I help you?")
    #  st.title("How can I help you?")
    

# with st.form("Input User Prompt"):
   

#     col1, col2 = st.columns([9, 1])

#     with col1:
#         st.text_input(
#             "Enter your message",
#             key="input_text",
#             placeholder=None,
#             label_visibility="collapsed",
            
#         )

#     with col2:
#         submit1 = st.form_submit_button(
#             label="", icon=":material/send:", on_click=clear_input
#         )
    
#     col4, col5, col6, col7 = st.columns(4)
    
#     with col4:
#         st.form_submit_button(
#             "Answer queries",
#             icon=":material/chat:",
#             on_click=Answer_queries,
#             use_container_width=True,
#         )
#     with col5:
#         st.form_submit_button(
#             "Get SHIELD report",
#             icon=":material/description:",
#             on_click=Get_SHIELD_report,
#             use_container_width=True,
#         )
#     with col6:
#         st.form_submit_button(
#             "Book site visit",
#             icon=":material/tour:",
#             on_click=Book_site_visit,
#             use_container_width=True,
#         )
#     with col7:
#         st.form_submit_button(
#             "Home loan sanction",
#             icon=":material/currency_rupee:",
#             on_click=Home_loan_sanction,
#             use_container_width=True,
#         )
#     st.markdown(
#         f""" 
#      <div style='color: #4c4848; font-size: 12px; text-align: center;'>
#            squarestAI can make mistakes. Check important info.
#      </div>
#      """,
#         unsafe_allow_html=True,
#     )
# for msg in st.session_state.messages:
#        st.chat_message(msg["role"]).write(msg["content"])
if len(st.session_state.messages) != 0:
    for msg in st.session_state.messages:
        if msg["role"]=="assistant": 
            st.chat_message(msg["role"], avatar="./icon.png").write(msg["content"])
        else :
            st.chat_message(msg["role"],avatar=":material/person:").write(msg["content"])
        
if prompt:=st.chat_input("Enter your Message"):
    # if len(st.session_state.messages)==0:
    #     container = placeholder.container(height=400, border = False)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    st.chat_message(name= "person",avatar=":material/person:").write(prompt)

    config = {"configurable": {"thread_id": "7896323"}}
    answer = rag.langgraph_agent_executor.invoke(
        {"messages": [("user", prompt)]},
        config,
    )["messages"][-1]

    msg = answer.content

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message(name="squarest", avatar="./icon.png").write(msg)
