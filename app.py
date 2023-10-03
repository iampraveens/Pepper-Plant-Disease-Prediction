import requests
from io import BytesIO
from PIL import Image

import numpy as np
import streamlit as st 
from tensorflow import keras
from keras.models import load_model

url = "https://cdn-icons-png.flaticon.com/512/3631/3631976.png"
response = requests.get(url)
image = Image.open(BytesIO(response.content))
page_title = 'Pepper Plant Disease Prediction'
page_icon = image
layout = 'wide'

st.set_page_config(page_title=page_title,
                   page_icon=page_icon,
                   layout=layout
                   )

hide_style = '''
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            <style>
            
            '''
header_style = '''
             <style>
             .navbar {
                 position: fixed;
                 top: 0;
                 left: 0;
                 width: 100%;
                 z-index: 1;
                 display: flex;
                 justify-content: center;
                 align-items: center;
                 height: 80px;
                 background-color: #239B56;
                 box-sizing: border-box;
             }
             
             .navbar-brand {
                 color: white !important;
                 font-size: 23px;
                 text-decoration: none;
                 margin-right: auto;
                 margin-left: 50px;
             }
             
             .navbar-brand img {
                margin-bottom: 6px;
                margin-right: 1px;
                width: 40px;
                height: 40px;
                justify-content: center;
            }
            
            /* Add the following CSS to change the color of the text */
            .navbar-brand span {
                color: #EF6E04;
                justify-content: center;
            }
            
             </style>
             
             <nav class="navbar">
                 <div class="navbar-brand">
                <img src="https://cdn-icons-png.flaticon.com/512/3631/3631976.png" alt="Logo">
                    Pepper Plant Disease Prediction
                 </div>
             </nav>
               '''
st.markdown(hide_style, unsafe_allow_html=True)
st.markdown(header_style, unsafe_allow_html=True)

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])


if uploaded_image is not None:
    column_1, column_2, column_3 = st.columns([35,10,70])
    
    with column_1:
        st.image(uploaded_image, caption="Uploaded Image", channels='RGB')
        predict_button = st.button(label='Predict Disease', type='secondary')
        
    with column_1:
        if predict_button:
            img = keras.preprocessing.image.load_img(uploaded_image, target_size=(256,256))
            img_array = np.array(img)
            img_array = img_array.reshape(1, 256, 256, 3)
            model = load_model('model.h5')
            
            prediction = model.predict(img_array)
            label = np.argmax(prediction[0])

            column_4, column_5 = st.columns([35,5])
            
            with column_4:
                if label == 0:
                    st.error("Plant is affected by bacteria")
                else:
                    st.success("Plant is healthy")
