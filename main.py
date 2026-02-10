import streamlit as st

st.header("EnlightenedAI")

agent = st.radio("Select style of Response: ", ["EnlightenedAI 0.0:0b", "Non-Dual", "Neo-Advaita", "JK"])


st.slider("Temperature: ", min_value = 0.0, max_value = 2.0, value = 1.0)
st.selectbox("Thinking: ", ['On', 'Off'])

question = st.text_area("Type your question: ")
if st.button("Submit"):
    if agent == "EnlightenedAI 0.0:0b":
        st.write("")
    elif agent == "Non-Dual":
        st.write("Who is the Submitter")
    elif agent == "Neo-Advaita":
        st.write("Disclaimer: There will be no spiritual progress with my answers.")
    elif agent == "JK":
        st.write("Submitter is the submitted.")