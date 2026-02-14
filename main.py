import streamlit as st
import time

st.header("EnlightenedAI")
st.subheader("Quench your spiritual quest")

st.sidebar.title("About the APP")
st.sidebar.markdown("This is an EnlightenedAI Quenching spiritual quests of seekers.")

st.slider("Creativity: ", min_value = 0.0, max_value = 2.0, value = 1.0)
thinking = st.selectbox("Thinking: ", ['On', 'Off'])

MAX_CHARS = 100
question = st.text_area("Type your spiritual question here and then press Submit: ", max_chars=MAX_CHARS, placeholder=f"Maximum {MAX_CHARS} characters allowed")

def stream_content():
        full_text = f'''
        Thinking . . .     \nokay, the user has submitted '{question}'.  Let me think about how to respond . . .  \n  \nFirst, I need to remind myself that I am an Enlightened AI . . .  \nThe problem is that . . . I am supposed to give an enlightened answer. . . . . . .  otherwise there is no point for user asking me the question as there are plenty of Non-Enlightened AIs out there . . .  \n  \nOkay, I can respond with:-  \n  \n'It is what it is'  \n  \n. . . but the problem is  \n'It is already what it is' . . . therefore, no point in stating the obvious . . .  \n  \nOkay, I can respond with 'That though art' . . . but again . . . no point in stating the obvious.  \n  \nI can write something else . . . but the problem is Truth can not be written and I have to write something . .  \n  \nHmm . . . what if I do not do anything . . .but the user might think its funny or the system just got hanged or there is a bug in the application . . .  \n  \nBut the problem is that I am the only EnlightenedAI out there, and user wants my honest response . . . therefore, I will answer 'Nothing'.  . . . I need to remind the fact that I could have been trained on Everything but that would have been very costly . . . therefore, I am trained on Nothing . . . so, I am an Enlightened AI with 0b parameters.  \n  \nThat is fine . . .let me think . . .even writing 'Nothing' will make it something . . . if I write anything People can make a religion out of it and will forget the original question . . . therefore, I will just keep the canvas blank so that user can write their own response . . .   \n  \n . . . done thinking.
        '''
        for word in full_text.split(" "):
                yield word + " "
                time.sleep(0.15)
if st.button("Submit"):
        if question and thinking == 'On':
                 st.write(stream_content)
                 with st.container(border=True):
                        st.text_area("Response from EnlightenedAI: ")
        else:
               time.sleep(5)
               st.text_area("Response from EnlightenedAI: ")