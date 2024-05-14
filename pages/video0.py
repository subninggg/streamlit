import streamlit as st
import time

col1, col2, col3 = st.columns(3)

with col1:
    st.write('원본 영상')
    st.video('https://file.notion.so/f/f/28b7e521-0e53-4f97-b19b-3c7008fb8ca0/4432775d-f722-42c8-b0af-f81d813f4180/ge_out21.mp4?id=28941da6-e5ad-4f5e-a205-d22c87109c4f&table=block&spaceId=28b7e521-0e53-4f97-b19b-3c7008fb8ca0&expirationTimestamp=1715731200000&signature=djcA-wxd14BRK1ZDfNRAxV9YbNxmOpkpebhkal-mJ_g&downloadName=ge_out21.mp4', format="video/mp4")

with col2:
    st.write('분석 영상')
    st.video('https://file.notion.so/f/f/2abd79a2-2684-43c4-88e8-dff82ccba814/411bbb86-3484-43a1-b5b7-811a97a77001/%EC%A0%9C%EB%AA%A9_%EC%97%86%EB%8A%94_%EB%8F%99%EC%98%81%EC%83%81_-_Clipchamp%EB%A1%9C_%EC%A0%9C%EC%9E%91.mp4?id=36c646e4-77c7-4843-9fa6-8787048f3e68&table=block&spaceId=2abd79a2-2684-43c4-88e8-dff82ccba814&expirationTimestamp=1715817600000&signature=0mBIFH03NKGHa-LAQUd7n-yJUbyaev_FhW6svHD-W-I&downloadName=%EC%A0%9C%EB%AA%A9+%EC%97%86%EB%8A%94+%EB%8F%99%EC%98%81%EC%83%81+-+Clipchamp%EB%A1%9C+%EC%A0%9C%EC%9E%91.mp4', format="video/mp4")
with col3:
    st.error('OUT')
    st.page_link("pages/video0_sttran.py", label="판정 분석")

st.write('분석 과정')
st.image('https://raw.githubusercontent.com/subninggg/streamlit/main/hiera_image/ge_out21_hiera.png')
