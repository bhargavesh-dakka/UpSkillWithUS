import streamlit as st
from streamlit_extras import switch_page_button
st.set_page_config("Upskill with us", "🏫",initial_sidebar_state="collapsed")

with open("page_style.css","r") as f:
    st.markdown(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)



st.columns(3)[1].image("assets//Upskill with us.png")
with st.container():
    st.header("""Upskill with us\n""")
    st.divider()
    st.markdown("""
Enhance your skills every day with our curated emails on a selected topic, complete with valuable references. Stay ahead of the curve and elevate your expertise in just a few minutes a day!\n
How it works:\n
* Choose a topic you want to upskill.
* Receive a daily email with concise insights and practical tips
* Explore additional resources and references for deeper learning
\n\nStart your upskilling journey today!""")
    if st.columns(5)[-1].button("Get Started"):
        switch_page_button.switch_page("service")

