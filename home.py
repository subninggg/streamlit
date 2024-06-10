# main.py
import streamlit as st
import pandas as pd

st.title('엘삼기 태그 아웃/세이프 판정 센터')
st.header('경기 기록')

option = st.selectbox(
    "요청팀",
    ("전체", "LG 트윈스", "KT 위즈", "SSG 랜더스", "NC 다이노스", "두산 베어스", "KIA 타이거즈", "롯데 자이언츠", "삼성 라이온즈", "한화 이글스", "키움 히어로즈")
)

LG = "https://ssl.gstatic.com/onebox/media/sports/logos/3NqgO_dpTThWu3KBf600tg_48x48.png"
KT = "https://ssl.gstatic.com/onebox/media/sports/logos/LUZj3ojt_H6lYisolvQ2pg_48x48.png"
SSG = "https://ssl.gstatic.com/onebox/media/sports/logos/171JeGI-4meYHLIoUPjerQ_48x48.png"
NC =  "https://ssl.gstatic.com/onebox/media/sports/logos/dDCbStDchWQktsZf2swYyA_48x48.png"
두산 = "https://ssl.gstatic.com/onebox/media/sports/logos/AP_sE5nmR8ckhs_zEhDzEg_48x48.png"
KIA = "https://ssl.gstatic.com/onebox/media/sports/logos/psd7z7tnBo7SD8f_Fxs-yg_48x48.png"
롯데 = "https://ssl.gstatic.com/onebox/media/sports/logos/cGrvIuBYzj4D6KFLPV1MBg_48x48.png"
삼성 = "https://ssl.gstatic.com/onebox/media/sports/logos/c_Jn4jW-NOwRtnGE7uQRAA_48x48.png"
한화 = "https://ssl.gstatic.com/onebox/media/sports/logos/pq5JUk7H0b6KX5Wi8M0xbA_48x48.png"
키움 = "https://ssl.gstatic.com/onebox/media/sports/logos/BXbvDpPIJZ_HpPL4qikxNg_48x48.png"

video0 = "https://github.com/subninggg/streamlit/blob/main/capture/ge_out21_crop.png?raw=true"
video1 = "https://github.com/subninggg/streamlit/blob/main/capture/ge_safe2_crop.png?raw=true"
video2 = "https://github.com/subninggg/streamlit/blob/main/capture/ge_safe20_crop.png?raw=true"
video3 = "https://github.com/subninggg/streamlit/blob/main/capture/ge_safe24_crop.png?raw=true"
video4 = "https://github.com/subninggg/streamlit/blob/main/capture/ge_safe28_crop.png?raw=true"
video5 = "https://github.com/subninggg/streamlit/blob/main/capture/jy_out4_crop.png?raw=true"
video6 = "https://github.com/subninggg/streamlit/blob/main/capture/sb_out4_crop.png?raw=true"
video7 = "https://github.com/subninggg/streamlit/blob/main/capture/sb_out5_crop.png?raw=true"
video8 = "https://github.com/subninggg/streamlit/blob/main/capture/sb_out24_crop.png?raw=true"
video9 = "https://github.com/subninggg/streamlit/blob/main/capture/sb_safe15_crop.png?raw=true"

video0_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video0"
video1_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video1"
video2_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video2"
video3_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video3"
video4_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video4"
video5_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video5"
video6_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video6"
video7_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video7"
video8_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video8"
video9_link = "https://homepy-wgogeawchtyohpnvkzfyzx.streamlit.app/video9"
if option == "전체":
    df = pd.DataFrame(
        {
            "home": [한화, KIA, KIA, 삼성, KIA, LG, 롯데, 롯데, KT, LG],
            "away": [롯데, KT, LG, KIA, LG, 삼성, LG, LG, 삼성, KIA],
            "call": ["out", "safe", "safe", "safe", "safe", "out", "out", "out", "out", "safe"],
            "video": [video0, video1, video2, video3, video4, video5, video6, video7, video8, video9],
            "link" : [video0_link, video1_link, video2_link, video3_link, video4_link, video5_link, video6_link, video7_link, video8_link, video9_link]
        }
    )
    st.dataframe(
        df,
        column_config={
            "home": st.column_config.ImageColumn(
                "홈"
            ),
            "away": st.column_config.ImageColumn(
                "원정"
            ),
            "call": "판정",
            "video": st.column_config.ImageColumn(
                "영상"
            ),
            "link": st.column_config.LinkColumn(
                "링크",
            )
        },
        hide_index=True,
    )
if option == "LG 트윈스":
    df = pd.DataFrame(
        {
            "home": [KIA, KIA, LG, 롯데, 롯데, LG],
            "away": [LG, LG, 삼성, LG, LG, KIA],
            "call": ["safe", "safe", "out", "out", "out", "safe"],
            "video": [video2, video4, video5, video6, video7, video9],
            "link" : [video2_link, video4_link, video5_link, video6_link, video7_link, video9_link]
        }
    )
    st.dataframe(
        df,
        column_config={
            "home": st.column_config.ImageColumn(
                "홈"
            ),
            "away": st.column_config.ImageColumn(
                "원정"
            ),
            "call": "판정",
            "video": st.column_config.ImageColumn(
                "영상"
            ),
            "link": st.column_config.LinkColumn(
                "링크",
            )
        },
        hide_index=True,
    )
if option == "KT 위즈":
    df = pd.DataFrame(
        {
            "home": [KIA, KT],
            "away": [KT, 삼성],
            "call": ["safe", "out"],
            "video": [video1, video8],
            "link" : [video1_link, video8_link]
        }
    )
    st.dataframe(
        df,
        column_config={
            "home": st.column_config.ImageColumn(
                "홈"
            ),
            "away": st.column_config.ImageColumn(
                "원정"
            ),
            "call": "판정",
            "video": st.column_config.ImageColumn(
                "영상"
            ),
            "link": st.column_config.LinkColumn(
                "링크",
            )
        },
        hide_index=True,
    )
if option == "SSG 랜더스":
    st.image('https://github.com/subninggg/streamlit/blob/main/update_image/SSG.png?raw=true')
if option == "NC 다이노스":
    st.image('https://github.com/subninggg/streamlit/blob/main/update_image/NC.png?raw=true')
if option == "두산 베어스":
    st.image('https://github.com/subninggg/streamlit/blob/main/update_image/%EB%91%90%EC%82%B0.png?raw=true')
if option == "KIA 타이거즈":
    df = pd.DataFrame(
        {
            "home": [KIA, KIA, 삼성, KIA, LG],
            "away": [KT, LG, KIA, LG, KIA],
            "call": ["safe", "safe", "safe", "safe", "safe"],
            "video": [video1, video2, video3, video4, video9],
            "link" : [video1_link, video2_link, video3_link, video4_link, video9_link]
        }
    )
    st.dataframe(
        df,
        column_config={
            "home": st.column_config.ImageColumn(
                "홈"
            ),
            "away": st.column_config.ImageColumn(
                "원정"
            ),
            "call": "판정",
            "video": st.column_config.ImageColumn(
                "영상"
            ),
            "link": st.column_config.LinkColumn(
                "링크",
            )
        },
        hide_index=True,
    )
if option == "롯데 자이언츠":
    df = pd.DataFrame(
        {
            "home": [한화, 롯데, 롯데],
            "away": [롯데, LG, LG],
            "call": ["out", "out", "out"],
            "video": [video0, video6, video7],
            "link" : [video0_link, video6_link, video7_link]
        }
    )
    st.dataframe(
        df,
        column_config={
            "home": st.column_config.ImageColumn(
                "홈"
            ),
            "away": st.column_config.ImageColumn(
                "원정"
            ),
            "call": "판정",
            "video": st.column_config.ImageColumn(
                "영상"
            ),
            "link": st.column_config.LinkColumn(
                "링크",
            )
        },
        hide_index=True,
    )
if option == "삼성 라이온즈":
    df = pd.DataFrame(
        {
            "home": [삼성, LG, KT],
            "away": [KIA, 삼성, 삼성],
            "call": ["safe", "out", "out"],
            "video": [video3, video5, video8],
            "link" : [video3_link, video5_link, video8_link]
        }
    )
    st.dataframe(
        df,
        column_config={
            "home": st.column_config.ImageColumn(
                "홈"
            ),
            "away": st.column_config.ImageColumn(
                "원정"
            ),
            "call": "판정",
            "video": st.column_config.ImageColumn(
                "영상"
            ),
            "link": st.column_config.LinkColumn(
                "링크",
            )
        },
        hide_index=True,
    )
if option == "한화 이글스":
    df = pd.DataFrame(
        {
            "home": [한화],
            "away": [롯데],
            "call": ["out"],
            "video": [video0],
            "link" : [video0_link]
        }
    )
    st.dataframe(
        df,
        column_config={
            "home": st.column_config.ImageColumn(
                "홈"
            ),
            "away": st.column_config.ImageColumn(
                "원정"
            ),
            "call": "판정",
            "video": st.column_config.ImageColumn(
                "영상"
            ),
            "link": st.column_config.LinkColumn(
                "링크",
            )
        },
        hide_index=True,
    )
if option == "키움 히어로즈":
    st.image('https://github.com/subninggg/streamlit/blob/main/update_image/%ED%82%A4%EC%9B%80.png?raw=true')
