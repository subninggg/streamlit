import streamlit as st

video_file = open('/home/vision/Capstone/video/video/ge_safe20.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)