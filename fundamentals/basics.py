import streamlit as st

# title
st.title("Title - Kamelsh")

# header
st.header("Header - Kamelsh")

# subheader
st.subheader("Subheader - Kamelsh")

# text
st.text("Text - Kamlesh")

# Markdown
st.markdown("This is list of h tags using markdown") # p
st.markdown("# Kamlesh")                             # h1
st.markdown("## Kamlesh")                            # h2
st.markdown("### Kamlesh")                           # h3
st.markdown("#### Kamlesh")                          # h4
st.markdown("##### Kamlesh")                         # h5
st.markdown("###### Kamlesh")                        # h6
st.markdown("####### Kamlesh")                       # print as it is

st.markdown('**GFG** is an Ed-Tech') # Bold
st.markdown('__GFG__ is an Ed-Tech') # Bold

st.markdown('*GFG* is an Ed-Tech') # Italic
st.markdown('_GFG_ is an Ed-Tech') # Italic


st.markdown('***GFG*** is an Ed-Tech') # Bold + Italic
st.markdown('___GFG___ is an Ed-Tech') # Bold + Italic

st.markdown('- First Point') # Unorder List
st.markdown('- Second Point')

st.write('Text is here') # Same as text
st.write(range(1, 10)) # function in write
st.text(range(1,10))   # function in text