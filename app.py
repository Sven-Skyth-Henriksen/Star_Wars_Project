from PIL import Image
import streamlit as st
from multiapp import MultiApp
from apps import about, home, data, graph # import your app modules here

app = MultiApp()



st.markdown("![title gif](https://media4.giphy.com/media/gXYlKennAlNfy/200w.webp?cid=ecf05e475f1zz2nhrj1xonfu9m5j6toky5akxiqi2ylxps84&rid=200w.webp&ct=g)")


st.markdown(' ## Team General Grievous welcomes you to our website')
st.text(' ')
st.markdown('----------------------------------------------- ')
st.text(' ')
st.text(' ')

st.markdown(' ')
st.markdown('##  MAY THE CODE BE WITH YOU   ')
st.markdown('----------------------------------------------- ')
st.markdown(' ')
st.markdown('Please select a page:')

# Add all your application here
app.add_app('Home',home.app)
app.add_app("About", about.app)
app.add_app("Data", data.app)
app.add_app('Galaxies Analysis', graph.app)
#app.add_app('Recommendation', tinker.app)



# The main app
app.run()