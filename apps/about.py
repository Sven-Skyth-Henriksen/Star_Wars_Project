from PIL import Image
import streamlit as st


def app():
    header = st.beta_container()
    image = st.beta_container()

    with header:
        st.title('🌐 Find the approx location of baby yoda is in the galaxy 🌐')     
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.title('⚜️ About ⚜️:')
        st.markdown('''
        
    
    We think there are 3 different galaxies in our clusters of data. We are trying to find them and  map them in this Project. We think that we can find baby yoda in the rightmost planet of this galaxy.
    
    
   ⬇️⬇️ This Project was created by 3 ***[Strive School](https://strive.school/)*** Students.⬇️⬇️
   
    ''')
    
        st.markdown('## Get to know us 👋🏻:')

    
        if st.button('Click here'):
            st.balloons()
            st.markdown("![Hello There](https://media3.giphy.com/media/fTI9mBoWLef8k/200w.webp?cid=ecf05e47zjdwnnnar41agsgibox4xavezp7ya6am6okj4b71&rid=200w.webp&ct=g)")
            st.write('***The Developer Team***:')
            st.write('• Deniz Elci: [GitHub ](https://github.com/Deniz-shelby)&[ LinkedIn](https://www.linkedin.com/in/deniz-elci-2500b2205/)')
            st.write('• Vladimir Gasanov: [GitHub ](https://github.com/VladimirGas)&[ LinkedIn](https://www.linkedin.com/in/vladimir-gasanov-1131b1134/)')
            st.write('• Sven Skyth Henriksen: [GitHub ](https://github.com/Sven-Skyth-Henriksen)&[ LinkedIn](https://www.linkedin.com/in/sven-skyth-henriksen-4857bb1a2/)')
            
        
    with image:
        image = Image.open('team.jpeg')
        st.image(image , caption='')