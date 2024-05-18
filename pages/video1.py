import streamlit as st
import time

col1, col2 = st.columns(2)

with col1:
    st.subheader('원본 영상')
    st.image('https://github.com/subninggg/streamlit/blob/main/video_gif/ge_safe2.gif?raw=true')

with col2:
    st.subheader('분석 영상')
    st.image('https://github.com/subninggg/streamlit/blob/main/hiera_gif/ge_safe2_hiera.gif?raw=true')

st.error('OUT')

st.subheader('')
st.subheader('분석 과정')
st.image('https://raw.githubusercontent.com/subninggg/streamlit/main/hiera_image/ge_safe2_hiera.png')

st.page_link("pages/video1_sttran.py", label="판정 분석")
