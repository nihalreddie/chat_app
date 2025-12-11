
import streamlit as st
from aireplay import get_instance,clear_instance
class Bot:
   
    def __init__(self):
        self.m= get_instance("Girl")
        

    def write_msg(self,new_message):
        if new_message:
            cleaned = new_message.strip()
            if not cleaned:
                st.warning("Please enter a message before sending.")
            else:
                sender = current_user if current_user else "Guest"
                self.m.get_response(cleaned)
        self.display()#
    
    def display(self):
        li=self.m.display_history()      
        if li==[]:
            pass
        else:            
                for i in range(len(li)):
                    if i%2==0:
                        with st.chat_message("user"):
                            st.write(li[i])
                    else:
                        with st.chat_message("ai"):
                            st.write(li[i])
                            #print(li[i])
        #print(li)

            


# Page configuration
st.set_page_config(
    page_title="Welcome to CHACHA",
    layout="wide"
)



# Reduce overall font size
st.markdown(
    """
    <style>
    html, body, [class*="css"]  {
        font-size: 12px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state
if 'username' not in st.session_state:
    st.session_state.username = []

if 'password' not in st.session_state:
    st.session_state.password = []

if 'auto_refresh' not in st.session_state:
    st.session_state.auto_refresh = True

# Get current user (fallback to Guest if none)
current_user = st.session_state.username[-1] if st.session_state.username else "Guest"

# Display the username
st.write(f"Welcome {current_user}")
b=Bot()



# Chat input for new messages
new_message = st.chat_input("Type your message here max 200 words")


if st.button("clear"):
    clear_instance()
    st.rerun()

b.write_msg(new_message)

