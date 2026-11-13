from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Stop, Clean & Go", layout="wide")

# Hilangkan padding bawaan Streamlit dan samakan latar dengan halaman
st.markdown(
    """
    <style>
    .stApp{background:#1A1A1A}
    header[data-testid="stHeader"]{display:none}
    .block-container{padding:0!important;max-width:100%!important}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).parent / "Stop_Clean_Go_fintech.html"
components.html(html.read_text(encoding="utf-8"), height=900, scrolling=True)
