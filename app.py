from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ciel et irradiance solaire",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """<style>
    header[data-testid="stHeader"], #MainMenu, footer {display:none !important;}
    .stApp {background:#07131f;}
    .block-container {padding:0 !important; max-width:none !important;}
    iframe {display:block; border:0;}
    </style>""",
    unsafe_allow_html=True,
)
html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=1220, scrolling=True)
