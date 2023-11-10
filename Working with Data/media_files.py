import streamlit as st
from PIL import Image

# Image
st.title("1.1> Image from path")
path = 'C:/Users/Kamlesh Baviskar/OneDrive/Desktop/Web-scrapping/Stock Images Scrapping/Imgs/Img-a-3049571__340.jpg.png'
img = Image.open(path)
st.image(img, width=50)

st.title("1.2> Image from Link")
st.image('https://www.sandeepmaheshwari.com/HomeBanner/2tv.jpg?v1.1')

# Video
st.title("2> Vedio")
video_file = open("file_example_MP4_480_1_5MG.mp4", "rb")
st.video(video_file, start_time=20)

# Audio
st.title("3> Audio")
video_file = open("file_example_MP3_700kb.mp3", "rb")
st.video(video_file)
