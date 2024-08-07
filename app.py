import streamlit as st
from PIL import Image
import pickle
import numpy as np

# Load the pickled model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
   
st.title('Rice Image Classification')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying the image")

    # Preprocess the image to match the model's expected input
    image = image.resize((128, 128))  # Resize to the size your model expects
    image = np.array(image) / 255.0  # Normalize the image
    image = image.reshape((1, 128, 128, 3))  # Reshape to add batch dimension

    # Make prediction
    prediction = model.predict(image)
    class_names = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']  # Replace with your actual class names
    predicted_class = class_names[np.argmax(prediction)]

    st.write(f'Predicted class: {predicted_class}')
