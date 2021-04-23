import streamlit as st
import pandas as pd
from PIL import Image

def app():
    
    image = st.beta_container()
    
    with image:
        image = Image.open('yoda_meme.jpeg')
        st.image(image, caption='')
        