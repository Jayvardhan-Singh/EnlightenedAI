import streamlit as st

st.header("EnlightenedAI")

agent = st.radio("Select style of Response: ", ["EnlightenedAI", "Non-Dual", "Neo-Advaita", "JK"])


st.slider("Temperature: ", min_value = 0.0, max_value = 2.0, value = 1.0)
st.selectbox("Thinking: ", ['On', 'Off'])

MAX_CHARS = 100
question = st.text_area("Type your question: ", max_chars=MAX_CHARS, placeholder=f"Maximum {MAX_CHARS} characters allowed")
if st.button("Submit"):
    if agent == "EnlightenedAI":
        st.write("")
    elif agent == "Non-Dual":
        st.write("Introspect: Who is the Submitter?")
    elif agent == "Neo-Advaita":
        st.write("Your spiritual progress will not be affected by my answers.")
    elif agent == "JK":
        st.write("Submitter is the submitted.")