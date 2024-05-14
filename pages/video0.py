import streamlit as st
import time

col1, col2, col3 = st.columns(3)

with col1:
    st.write('원본 영상')
    st.video('https://file.notion.so/f/f/28b7e521-0e53-4f97-b19b-3c7008fb8ca0/4432775d-f722-42c8-b0af-f81d813f4180/ge_out21.mp4?id=28941da6-e5ad-4f5e-a205-d22c87109c4f&table=block&spaceId=28b7e521-0e53-4f97-b19b-3c7008fb8ca0&expirationTimestamp=1715731200000&signature=djcA-wxd14BRK1ZDfNRAxV9YbNxmOpkpebhkal-mJ_g&downloadName=ge_out21.mp4', format="video/mp4")

with col2:
    st.write('분석 영상')
    st.video('https://file.notion.so/f/f/2abd79a2-2684-43c4-88e8-dff82ccba814/543732dd-1e51-42e0-abe9-b6a116fe06a5/jy_out4.mp4?id=e28a2c06-0390-4547-9f22-69e5f21b54a1&table=block&spaceId=2abd79a2-2684-43c4-88e8-dff82ccba814&expirationTimestamp=1715817600000&signature=iEkcQyxkDII7mxwbKt2EZ45LYXVHU_y0VOEKXJGkC78&downloadName=jy_out4.mp4', format="video/mp4")
with col3:
    st.error('OUT')
    st.page_link("pages/video0_sttran.py", label="판정 분석")

st.write('분석 과정')
st.image('https://raw.githubusercontent.com/subninggg/streamlit/main/hiera_image/ge_out21_hiera.png')
