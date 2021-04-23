import streamlit as st
import pandas as pd
from PIL import Image

def app():
    
    text = st.beta_container()
    image = st.beta_container()
   
    
    
    with text:
        st.markdown(''' 
        ### We thank you for your time and patience.
        ### We hope that you will have a nice day and... 
        ''')
        st.text(' ')
        st.text(' ')
        st.markdown('----------------------------------------------- ')
    
    with image:
        image = Image.open('the_force.jpeg')
        st.image(image, caption='')