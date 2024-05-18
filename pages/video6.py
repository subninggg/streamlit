import streamlit as st
import time

col1, col2, col3 = st.columns(3)

with col1:
    st.write('원본 영상')
    st.image('https://github.com/subninggg/streamlit/blob/main/video_gif/sb_out4.gif?raw=true')

with col2:
    st.write('분석 영상')
    st.image('https://github.com/subninggg/streamlit/blob/main/hiera_gif/sb_out4_hiera.gif?raw=true')
with col3:
    st.error('OUT')
    st.page_link("pages/video6_sttran.py", label="판정 분석")

st.write('분석 과정')
st.image('https://raw.githubusercontent.com/subninggg/streamlit/main/hiera_image/sb_out4_hiera.png')
