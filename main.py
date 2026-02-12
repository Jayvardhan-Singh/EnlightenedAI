import streamlit as st
import time

st.header("EnlightenedAI")
st.subheader("Satisfy your spiritual quest")

st.slider("Temperature: ", min_value = 0.0, max_value = 2.0, value = 1.0)
thinking = st.selectbox("Thinking: ", ['On', 'Off'])

MAX_CHARS = 100
question = st.text_area("Type your question: ", max_chars=MAX_CHARS, placeholder=f"Maximum {MAX_CHARS} characters allowed")

def stream_content():
        full_text = f". . . thinking . . .     \nthe user has asked '{question}'... but the problem is that i am an EnlightenedAI . . .  . . .  . . . i am supposed to give the enlightened answer. . . .  \n  \n. . .  otherwise there is no point in asking me the question . . .  \n. . .  there are plenty of Non Enlightened AIs out there  \n ...done thinking."
        for word in full_text.split(" "):
                yield word + " "
                time.sleep(0.15)
if st.button("Submit"):
        if question and thinking == 'On':
                 st.write(stream_content)