import streamlit as st
from openai import OpenAI

st.title("Tismo Interview Prep Chatbot")
st.write(
    "This chatbot helps you prepare for Tismo interviews, covering computer architecture, microcontrollers, digital/analog electronics, and CS questions."
)

# Ask user for OpenAI API key
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Check if API key is provided
if openai_api_key:
    # Create OpenAI client
    client = OpenAI(api_key=openai_api_key)

    # Chat input from user
    user_input = st.text_area("Enter your query or topic for discussion:")

    if st.button("Generate Response"):
        # Construct prompt with user input
        prompt = f"During Tismo's interviews, candidates are often tested on several technical topics. They include:\n\n{user_input}"

        # Call OpenAI API to generate response
        response = client.completions.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            top_p=1.0,
            stop=None
        )

        # Display AI response
        st.subheader("AI Response:")
        st.write(response["choices"][0]["text"])

else:
    st.warning("Please enter your OpenAI API Key to continue.")
