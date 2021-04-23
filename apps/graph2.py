import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px


def app():

    media = st.beta_container()
    image = st.beta_container()


    with media:
        # Another1

        with st.beta_expander('• Wanna see the Principal Component Analysis ? CLICK HERE!'):
            image = Image.open('PCA.jpeg')
            st.image(image , caption='')
            st.markdown(''' 
            We use PCA for dimensionality reduction. Our Machine learning Model becomes ***more efficient*** with this method.
            ''')

            

        # Another1
        with st.beta_expander('• If u want to see the planets and the center of gravity ? CLICK HERE! '):
            image = Image.open('maping.jpeg')
            st.image(image , caption='')
            st.markdown(''' 
            As you can see, we have another 6 clusters which represent the planets. The orange point in the bottem cluster represent the center of gravity.
            ''')
            
        with st.beta_expander("• Here is baby yoda's location. CLICK HERE!"):
            image = Image.open('location.jpeg')
            st.image(image , caption='')
            st.markdown(''' 
            The green point on the graph represents the neares point to the orange one so that means that we can find baby yoda on this coordinates: ***[-0.14618598571053917 , -0.0314798954338306]***
            ''')        
           
app()
