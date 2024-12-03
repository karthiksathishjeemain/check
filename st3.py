# import streamlit as st
# # st.container(height=300)
# messages = st.container(height=300)
# # if "messages"
# if "inout" not in st.session_state:
#     st.session_state.inout = [{"role":"ass","con":"Search now"}]
# for ms in st.session_state.inout:
#     messages.chat_message(ms.role).write(ms.con)
#     messages.chat_message(ms.role).write(ms.con)
# if prompt := st.chat_input("Say something"):
#         st.session_state.inout.append({"role":"user","con": prompt})
#         st.session_state.inout.append({"role":"ass","con":"echo "+ prompt})
#         messages.chat_message("user").write(prompt)
#         messages.chat_message("assistant").write(f"Echo: {prompt}")
import streamlit as st
footer = """
<style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #a1918e;
    }
</style>
<div class="footer">
  SQUAREST AI may produce false outputs.
</div>
"""
messages = st.container(height=300)

st.markdown(footer, unsafe_allow_html=True)
# Initialize session state for messages
if "inout" not in st.session_state:
    st.session_state.inout = [{"role": "assistant", "con": "Search now"}]

# Display messages

# with messages:
# st.markdown("<div style='position: fixed; bottom: 0;         color: #a1918e;left: 0;'>SQAREST AI may be wrong sometimes</div>", unsafe_allow_html=True)
for ms in st.session_state.inout:
        messages.chat_message(ms["role"]).write(ms["con"])

# Input for new messages
if prompt := st.chat_input("Say something"):
    # Append new user message
    st.session_state.inout.append({"role": "user", "con": prompt})
    # Append assistant's response
    st.session_state.inout.append({"role": "assistant", "con": f"Echo: {prompt}"})
    messages.chat_message("user").write(prompt)
    messages.chat_message("assistant").write(f"exho: {prompt}")
footer = """
<style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #a1918e;
    }
</style>
<div class="footer">
  SQUAREST AI may produce false outputs.
</div>
"""
st.markdown(footer, unsafe_allow_html=True)