import streamlit as st
import time
from PIL import Image

def img_converter(old_image, new_img_fmt):
    image = Image.open(old_image)
    img_name = old_image.name.split('.')[0]
    # st.write(img_name)
    file_name = img_name+"."+new_img_fmt
    new_img = image.convert("RGB")
    new_img.save(file_name)
    # time.sleep(5)
    with st.empty():
        st.write("Processing... ")
        time.sleep(.3)
        st.write("Checking for availability... ")
        time.sleep(.4)
        time.sleep(.3)
        for i in range(1, 100):
            st.progress(i, text="Converting your image...")
            time.sleep(.1)

    st.success("Image conversion successfull!")
    st.balloons()


img_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
if img_file is not None:
    st.image(img_file, width=150)
img_formate = st.selectbox("Select output image format", ['png', "jpg", "jpeg"])


btn = st.button("Convert")
if btn:
    if img_file is None:
        st.error("Please upload Image file first.")
    img_converter(img_file, img_formate)


