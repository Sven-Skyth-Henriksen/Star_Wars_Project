import streamlit as st
import pandas as pd
from PIL import Image

def app():
    
    data = st.beta_container()
    
    dx = pd.read_csv('planet.csv')
    df = pd.read_csv('galaxies.csv')

    with data:
        st.write("""In this project, we navigate through Star Wars Galaxy data to find baby yoda's location. From the data, 
     we got some interesting insights that you might be curious to know and stored the answers in a readable format for your convinience.""")
        st.markdown('Here you can find the source code : [Star_Wars_Project](https://github.com/Sven-Skyth-Henriksen/Star_Wars_Project)')
        st.title('Data')
        st.markdown("![Data](https://media3.giphy.com/media/4FQMuOKR6zQRO/giphy.webp?cid=ecf05e47teulwamthzfh5rqgji0j4nmfxw1b52c2rgsybk50&rid=giphy.webp&ct=g)")

        if st.checkbox('Reveal the data'):
            st.subheader('Galaxies coordinates')
            st.write(df) #.header(50) inside the the ()
            st.subheader('Planets coordinates')
            st.write(dx) #.header(50) inside the the ()
        
            
                    
