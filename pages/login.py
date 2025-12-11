import streamlit as st

st.title("Welcome")

if 'username' not in st.session_state:
    st.session_state.username=[]

if 'password' not in st.session_state:
    st.session_state.password=[]

user_name=st.text_input(label="Username",placeholder="enter Email ID or User Name",max_chars=25)
st.session_state.username.append(user_name)

#passwd=st.text_input(label="Password",type='password',placeholder="enter Password",max_chars=15)
#st.session_state.password.append(passwd)

if st.button("Login"):
   st.switch_page("pages/dash.py")