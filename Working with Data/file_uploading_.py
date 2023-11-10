import streamlit as st
from PIL import Image

st.title("File Uploading")

# Image
st.subheader("1. Uploading an Image")
img_file = st.file_uploader("Upload Image", type= ['png', 'jpeg'])
if img_file is not None:
    # st.write(type(img_file))

    file_details = {'file_name':img_file.name, 'file_type':img_file.type,
                    'file_size':img_file.size}
    st.write(file_details)

    st.image(Image.open(img_file))

# Audio
st.subheader("2. Uploading an Audio")
aud_file = st.file_uploader("Upload Audio", type= ['wav', 'mp3'])
if aud_file is not None:
    # st.write(type(img_file))

    file_details = {'file_name':aud_file.name, 'file_type':aud_file.type,
                    'file_size':aud_file.size}
    st.write(file_details)

    st.audio(aud_file)

# Video
st.subheader("3. Uploading an Vedio")
vid_file = st.file_uploader("Upload Vedio", type= ['mov', 'mp4'])
if vid_file is not None:
    # st.write(type(img_file))

    file_details = {'file_name':vid_file.name, 'file_type':vid_file.type,
                    'file_size':vid_file.size}
    st.write(file_details)

    st.video(vid_file)

# CSV
st.subheader("4. Uploading an CSV")
data_file = st.file_uploader("Upload CSV", type= ['csv', 'xlsx'])
if data_file is not None:
    # st.write(type(img_file))

    file_details = {'file_name':data_file.name, 'file_type':data_file.type,
                    'file_size':data_file.size}
    st.write(file_details)

    st.dataframe(data_file)