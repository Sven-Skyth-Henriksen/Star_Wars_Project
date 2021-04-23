import streamlit as st
import pandas as pd
from PIL import Image

def app():
    
    data = st.beta_container()
    

    df = pd.read_csv('galaxies.csv')

    with data:
        st.write("""In this project, we navigate through Star Wars Galaxy data to find baby yoda's location. From the data, 
     we got some interesting insights that you might be curious to know and stored the answers in a readable format for your convinience.""")
        st.title('Data')
        st.markdown("![Data](https://media4.giphy.com/media/xT9C25UNTwfZuk85WP/200.webp?cid=ecf05e47844brv5239cczg9hqo5ernebyirvx4xaua7k2dk8&rid=200.webp&ct=g)")

        if st.checkbox('Reveal The Library'):
            st.subheader('Books')
            st.write(df) #.header(50) inside the the ()
    
                    
