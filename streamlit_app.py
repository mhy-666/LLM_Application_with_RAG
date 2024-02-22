import streamlit as st

from src.LLMs import get_chat_answer
from openai import AzureOpenAI
import os
from src.retrieval import topk_retrieval, get_chunk_ids
from setup import set_up

st.title("League of Legends Wiki App")

database = set_up()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),  
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "RAG-gpt-35"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        _, context = topk_retrieval(
            ids=get_chunk_ids(), query=prompt, index=database, k=5
        )
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})