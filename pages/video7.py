import streamlit as st

video_file = open('/home/vision/Capstone/video/video/sb_out5.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)