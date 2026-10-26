# app.py
import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Road Safety Policy Agent", page_icon="🚦")
st.title("🚦 Road Safety Policy Agent")
st.caption("Based on TOI editorial 'Sense & Licence'. Not legal advice.")

default_q = (
    "Why do road deaths rise despite stricter rules, and which "
    "enforcement-focused policies could reduce them in India?"
)
question = st.text_area("Policy question", value=default_q, height=100)

if st.button("Analyse"):
    with st.spinner("Agent is gathering evidence and drafting recommendations..."):
        answer = run_agent(question, verbose=False)
    st.markdown(answer)