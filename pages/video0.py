import streamlit as st
import time

col1, col2, col3 = st.columns(3)

with col1:
    st.write('원본 영상')
    st.video('https://youtu.be/Dan-UpqtzL4?si=VfdQ9MRT4e7F2SH9', format="video/mp4")

with col2:
    st.write('분석 영상')
    st.video('https://youtu.be/Dan-UpqtzL4?si=VfdQ9MRT4e7F2SH9', format="video/mp4")
with col3:
    st.error('OUT')


st.write('분석 과정')
#st.image('/home/vision/Capstone/video/hiera_image/ge_out21_hiera.png')
