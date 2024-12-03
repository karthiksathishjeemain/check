import streamlit as st

# Add some scrollable content
st.title("Page with Scrollable Content")
st.write("This is a demo for scrolling content with a fixed header.")
for i in range(100):
    st.write(f"Line {i+1}")

# Add a sticky header using CSS
header = """
<style>
    .header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding-top: 50px;
        # margin-top : 100000 px;
        font-size: 20px;
        color: #a1918e;
        z-index: 1000; /* Ensure it's above other elements */
    }
    /* Add margin to the body to avoid overlap with the fixed header */
   
</style>
<div class="header">
    This is a fixed header. It stays at the top!
</div>
<div class="main">
</div>
"""
st.markdown(header, unsafe_allow_html=True)
