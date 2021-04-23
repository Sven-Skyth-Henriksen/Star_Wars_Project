import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px


def app():

    media = st.beta_container()
    image = st.beta_container()

    with media:
        # Another1

        with st.beta_expander('• Wanna see the different galaxies ? CLICK HERE!'):
            image = Image.open('uppermost.jpeg')
            st.image(image , caption='')
            st.markdown(''' 
            Here you can see that each cluster represent a ***different*** galaxy.
            ''')

            

        # Another1
        with st.beta_expander('• Curious about the uppermost Galaxy ? CLICK HERE! '):
            image = Image.open('galaxy.jpeg')
            st.image(image , caption='')
            st.markdown(''' 
            Uppermost Galaxy has the centroid coordinates: ***[5.46605246 , 9.68163004]***
            ''')
            
            
            




app()
