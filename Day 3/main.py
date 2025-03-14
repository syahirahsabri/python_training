import streamlit as st



st.set_page_config(page_title="test", page_icon=":shark:",layout="wide")
from PIL import Image
im = Image.open("../Day 3/shrdc_logo.png")
st.image(im, width=300)
st.markdown("Hello World!")




