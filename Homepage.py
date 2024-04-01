import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = None
if "MOONSHOT_API_KEY" not in st.session_state:
    st.session_state["MOONSHOT_API_KEY"]=""
else:
    chat = ChatOpenAI(openai_api_key = st.session_state["OPENAI_API_KEY"])

if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"]=""

st.set_page_config(page_title="Welcome to ASL",layout="wide")
st.title("😀Welcome to ASL")

# with st.container():
#     st.header("OpenAI Settings")
#     st.markdown(f"""
#         | OpenAI API Key |
#         | -------------- |
#         | {st.session_state["OPENAI_API_KEY"]} |
#                 """)

# with st.container():
#     st.header("MoonShot Settings")
#     st.markdown(f"""
#         | MoonShot API Key |
#         | -------------- |
#         | {st.session_state["MOONSHOT_API_KEY"]} |
#                 """)
    

if chat:
    with st.container():
        st.header("Chat with GPT")
        prompt = st.text_input("Prompt",value="", max_chars=None, key=None,type="default")
        asked = st.button("Ask")
        if asked:
            ai_message = chat([HumanMessage(content=prompt)])
            st.write(ai_message.content)
else:
    with st.container():
        st.warning("Please set your OpenAI key in the settings page.")