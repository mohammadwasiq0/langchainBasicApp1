
import streamlit as st


# from langchain_openai import ChatOpenAI

#import os
#os.environ["OPENAI_API_KEY"] = "sk-PLfFw23dd932dfg34446dftyvvdfgdfgmvXr2dL8hVowXdt"

HUGGINGFACEHUB_API_TOKEN= "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"

from huggingface_hub import login
login(token = HUGGINGFACEHUB_API_TOKEN)

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# From here down is all the StreamLit UI
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Hey, I'm your Chat GPT")



if "sessionMessages" not in st.session_state:
     st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful assistant.")
    ]



def load_answer(question):

    st.session_state.sessionMessages.append(HumanMessage(content=question))

    assistant_answer  = chat.invoke(st.session_state.sessionMessages )

    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))

    return assistant_answer.content


def get_text():
    input_text = st.text_input("You: ")
    return input_text


# chat = ChatOpenAI(temperature=0)

from langchain_huggingface import HuggingFaceEndpoint
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

chat = HuggingFaceEndpoint(
    repo_id=repo_id,
    max_length=128,
    temperature=0.7,
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
)
# llm_chain = prompt | llm
# print(llm_chain.invoke({"question": question}))




user_input=get_text()
submit = st.button('Generate')  

if submit:
    
    response = load_answer(user_input)
    st.subheader("Answer:")

    st.write(response)

