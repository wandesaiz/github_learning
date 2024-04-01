import streamlit as st
if "MOONSHOT_API_KEY" not in st.session_state:
    st.session_state["MOONSHOT_API_KEY"]=""
st.set_page_config(page_title="Moonshot Settings",layout="wide")

st.title("MoonShot Settings")

moonshot_api_key = st.text_input("API key", value = st.session_state["MOONSHOT_API_KEY"],max_chars=None, key= None, type="default" )
save = st.button("Save")

if save:
    st.session_state["MOONSHOT_API_KEY"] = moonshot_api_key