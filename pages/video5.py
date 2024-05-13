import streamlit as st

video_file = open('/home/vision/Capstone/video/video/jy_out4.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)