import streamlit as st
import datetime

st.title('LSK 2024')
st.header('태그 판정')

genre = st.radio(
    "판정",
    [":red[out]", ":green[safe]"],
)