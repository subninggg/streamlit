import streamlit as st
import time

col1, col2 = st.columns(2)

with col1:
    st.write('원본 영상')
    st.image('https://github.com/subninggg/streamlit/blob/main/video_gif/ge_out21.gif?raw=true')

with col2:
    st.write('분석 영상')
    st.image('https://github.com/subninggg/streamlit/blob/main/hiera_gif/ge_out21_hiera.gif?raw=true')

st.error('OUT')
st.page_link("pages/video0_sttran.py", label="판정 분석")

st.write('분석 과정')
st.image('https://raw.githubusercontent.com/subninggg/streamlit/main/hiera_image/ge_out21_hiera.png')
