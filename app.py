from PIL import Image
import streamlit as st
from multiapp import MultiApp
from apps import about, home, data # import your app modules here

app = MultiApp()



st.markdown("![Alt Text](https://media4.giphy.com/media/kAUgtSozkruPC/giphy.gif?cid=ecf05e479pk2ussq7xsuj51wmqguurjnhf3bl30j7v4atlbw&rid=giphy.gif&ct=g)")


st.title(' Team General Grievious welcomes you to our website')
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
#app.add_app('Data Analysis', graph.app)
#app.add_app('Recommendation', tinker.app)



# The main app
app.run()