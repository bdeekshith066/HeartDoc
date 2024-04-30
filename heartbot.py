import streamlit as st
import time
import random

def app():
    

    # Introduction
    gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 3em;
        }
        </style>
        <div class="gradient-text">Heading</div>
        """

    st.markdown(gradient_text_html, unsafe_allow_html=True) 
    st.write('Ask all your doubts to chatbot') 

    def response_generator():
        response = random.choice(
            [
                "Hello there! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        )
        for word in response.split():
            yield word + " "
            time.sleep(0.05)


    

    # Initialize chat history
    if "branch_messages" not in st.session_state:
        st.session_state.branch_messages = [{"role": "assistant", "content": "Hi! Which branch are you curious about?"}]

    # Display chat messages from history on app rerun
    for message in st.session_state.branch_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("enter your queries"):
        # Add user message to chat history
        st.session_state.branch_messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state.branch_messages.append({"role": "assistant", "content": response})



if __name__ == "__main__":
    app()