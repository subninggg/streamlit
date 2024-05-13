import streamlit as st
import time

col1, col2, col3 = st.columns(3)

with col1:
    st.write('원본 영상')
    video_file = open('https://youtu.be/Dan-UpqtzL4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
with col2:
    st.write('분석 영상')
    hiera_video_file = open('/home/vision/Capstone/video/hiera_video/ge_out21_hiera.mp4', 'rb')
    hiera_video_bytes = hiera_video_file.read()

    st.video(hiera_video_bytes)
with col3:
    st.error('OUT')


st.write('분석 과정')
st.image('/home/vision/Capstone/video/hiera_image/ge_out21_hiera.png')
