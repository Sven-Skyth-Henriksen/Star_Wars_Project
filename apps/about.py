from PIL import Image


def app():
    header = st.beta_container()
    image = st.beta_container()

    with header:
        st.title('Books That Everyone Should Read At Least Once\n')     
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.title('⚜️ About ⚜️:')
        st.markdown('''
    
    Books are available for everyone, rich and poor, young and old. 
    From love stroys to Sci Fi, it's gonna change the world for 
    everyone. How will your life be affected ?📖
    
   ⬇️⬇️ This Project was created by 4 ***[Strive School](https://strive.school/)*** Students.⬇️⬇️
    ''')
    
        st.markdown('## Get to know us 👋🏻:')

    
        if st.button('Click here'):
            st.balloons()
            st.markdown("![Hello There](https://media2.giphy.com/media/3ornk57KwDXf81rjWM/200w.webp?cid=ecf05e47chobelyn3nvbi5od5v1l7ahhd8t9uy1irct4rqiq&rid=200w.webp&ct=g)")
            st.write('***The Developer Team***:')
            st.write('• Deniz Elci: [GitHub ](https://github.com/Deniz-shelby)&[ LinkedIn](https://www.linkedin.com/in/deniz-elci-2500b2205/)')
            st.write('• Vladimir Gasanov: [GitHub ]()&[ LinkedIn](https://www.linkedin.com/in/vladimir-gasanov-1131b1134/)')
            st.write('• Sven Skyth Henriksen: [GitHub ](https://github.com/Sven-Skyth-Henriksen)&[ LinkedIn](https://www.linkedin.com/in/sven-skyth-henriksen-4857bb1a2/)')
            
        
    with image:
        image = Image.open('')
        st.image(image , caption='')