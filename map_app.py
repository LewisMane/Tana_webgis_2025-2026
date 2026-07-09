import streamlit as st
import streamlit.components.v1 as components

# Full-screen layout, no sidebar padding
st.set_page_config(page_title="TWWDA Projects", layout="wide")

# Hide Streamlit's default padding/menu/footer so it feels like a standalone map
st.markdown("""
    <style>
        .block-container {padding: 0 !important; margin: 0 !important;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Load your exported HTML map
with open("map_3.html", "r", encoding="utf-8") as f:
    map_html = f.read()

# Render it to fill the browser window
components.html(map_html, height=1000, scrolling=True)
