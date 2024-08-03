import streamlit as st
from streamlit_extras import switch_page_button
import groq
import yagmail
st.set_page_config("Upskill with us", "🏫",initial_sidebar_state="collapsed")

def send_email(email, text):
    client = yagmail.SMTP(st.secrets["email"], st.secrets["password"])
    client.send(email,"Upskill Now", text)

with open("page_style.css","r") as f:
    st.markdown(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)


st.columns(3)[1].image("assets//Upskill with us.png")
with st.container(height= 500):
    st.title("Upskill with us")
    email = st.text_input("Enter your email to recieve updates*",help="Your emails are safe with us.",)
    topic_name = st.text_input("Enter your topic name*")
    frequency  = st.radio("How frequently you want to recieve the next scedule update?*",["Daily","Weekly"])

    if st.button("Subscribe"):
        client = groq.Groq(api_key=st.secrets["api_key"]).chat.completions.create(
            model = "llama3-8b-8192",
            messages=[{
                "role": "system",
                "content" : "You are a smart assistant to help everyone in upskilling on provided topic name with Schedule and reference links and supporting youtube videos and content to study" 
            },
            {
                "role": "user",
                "content": f"Hi, I am interested in upskilling on {topic_name}"
            }
            ]
        )
        body_message = client.choices[0].message.content.replace("**","\n")
        print(body_message)
        send_email(email, body_message)
        st.success("Subscribed.. ")

