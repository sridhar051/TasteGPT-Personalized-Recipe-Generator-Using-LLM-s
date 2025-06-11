import os
import streamlit as st
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("TasteGPT: Recipe Generator")

prompt = st.text_input("Describe the ingredients or dish you want")

if st.button("Generate"):
    if not openai.api_key:
        st.error("OPENAI_API_KEY environment variable not set")
    elif prompt:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Give me a recipe: {prompt}"}],
        )
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter a prompt")
