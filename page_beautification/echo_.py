import streamlit as st

def get_username():
    return "Kamlesh"
# echo command
with st.echo():
    def get_punc():
        return "!!!"
    greeting = "Hi there, "
    name = get_username()
    punch = get_punc()
    st.write(greeting, name, punch)

# stop command
first_name = st.text_input("Enter your first name :")
if not first_name:
    st.warning("Please enter your first name.")
    st.stop()
last_name = st.text_input("Enter your larst name :")
if not last_name:
    st.warning("Please enter your last name.")
else:
    st.success("Thanks for filling form!")