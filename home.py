# main.py
import streamlit as st
import datetime

st.title('LSK 2024')

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/경기기록.py", label="경기기록")
with col2:
    st.page_link("pages/태그 판정.py", label="태그 판정")

st.page_link("https://www.kborc.com/main.do", label="KBO 비디오판독센터")
