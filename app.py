import streamlit as st
from img_classification import teachable_machine_classification
import keras
from PIL import Image, ImageOps
import numpy as np

uploaded_file = st.file_uploader("Carga una imagen ...", type=["jpg","jpeg"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  label = teachable_machine_classification(image, 'keras_model.h5') 
  st.write(label)
  st.image(image)

  if label == 0:
    result = "Enojadote"
  elif label ==1:
    result = "Feliz"
  elif label ==2:
    result = "Relajado"
  else:
    result = "Triste" 
st.subheader("El :dog: esta: "+ result)
