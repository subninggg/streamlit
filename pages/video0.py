import streamlit as st
import time

col1, col2, col3 = st.columns(3)

with col1:
    st.write('원본 영상')
    st.video('https://file.notion.so/f/f/28b7e521-0e53-4f97-b19b-3c7008fb8ca0/4432775d-f722-42c8-b0af-f81d813f4180/ge_out21.mp4?id=28941da6-e5ad-4f5e-a205-d22c87109c4f&table=block&spaceId=28b7e521-0e53-4f97-b19b-3c7008fb8ca0&expirationTimestamp=1715731200000&signature=djcA-wxd14BRK1ZDfNRAxV9YbNxmOpkpebhkal-mJ_g&downloadName=ge_out21.mp4', format="video/mp4")

with col2:
    st.write('분석 영상')
    st.video('https://file.notion.so/f/f/2abd79a2-2684-43c4-88e8-dff82ccba814/0296b0d3-38a0-4cd1-af82-a17c0db68778/ge_out21_hiera.mp4?id=e0cf9e81-396f-4bab-b838-0265b3425139&table=block&spaceId=2abd79a2-2684-43c4-88e8-dff82ccba814&expirationTimestamp=1715817600000&signature=K2Bvg6K1X29rN1jBpfcXHPSPHVkIJ-KRJapwG92OEdw&downloadName=ge_out21_hiera.mp4', format="video/mp4")
with col3:
    st.error('OUT')
    st.page_link("pages/video0_sttran.py", label="판정 분석")

st.write('분석 과정')
st.image('https://raw.githubusercontent.com/subninggg/streamlit/main/hiera_image/ge_out21_hiera.png')
