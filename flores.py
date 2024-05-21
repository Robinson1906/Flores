# streamlit_audio_recorder y whisper by Alfredo Diaz - version Mayo 2024

# En VsC seleccione la version de Python (recomiendo 3.9) 
#CTRL SHIFT P  para crear el enviroment (Escriba Python Create Enviroment) y luego venv 

#o puede usar el siguiente comando en el shell
#Vaya a "view" en el menú y luego a terminal y lance un terminal.
#python -m venv env

#Verifique que el terminal inicio con el enviroment o en la carpeta del proyecto active el env.
#cd D:\flores\env\Scripts\
#.\activate 

#Debe quedar asi: (.venv) D:\proyectos_ia\Flores>

#Puedes verificar que no tenga ningun libreria preinstalada con
#pip freeze
#Actualicie pip con pip install --upgrade pip

#pip install tensorflow==2.15 La que tiene instalada Google Colab o con la versión qu fué entrenado el modelo
#Verifique se se instaló numpy, no trate de instalar numpy con pip install numpy, que puede instalar una version diferente
#pip install streamlit
#Verifique se se instaló no trante de instalar con pip install pillow
#Esta instalacion se hace si la requiere pip install opencv-python

#Descargue una foto de una flor que le sirva de ícono 

# importing the libraries and dependencies needed for creating the UI and supporting the deep learning models used in the project
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import streamlit as st  
import tensorflow as tf # TensorFlow is required for Keras to work
from PIL import Image
import numpy as np
#import cv2

# hide deprication warnings which directly don't affect the working of the application
import warnings
warnings.filterwarnings("ignore")

# set some pre-defined configurations for the page, such as the page title, logo-icon, page loading state (whether the page is loaded automatically or you need to perform some action for loading)
st.set_page_config(
    page_title="Reconocimiento de Flores",
    page_icon = ":smile:",
    initial_sidebar_state = 'auto'
)
