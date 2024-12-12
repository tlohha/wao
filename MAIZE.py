import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the trained model
model = load_model("maize_disease_model.h5")

# Disease labels and treatment recommendations
disease_labels = {
    0: ("Healthy", "No treatment needed."),
    1: ("Gray Leaf Spot", "Use fungicides like Azoxystrobin or Pyraclostrobin."),
    2: ("Common Rust", "Apply fungicides containing Mancozeb or Chlorothalonil."),
    3: ("Northern Leaf Blight", "Use fungicides like Propiconazole or Tebuconazole."),
}

# Image size for the model
image_size = (224, 224)

# Streamlit UI
st.title("Maize Crop Disease Detection")
st.write("Upload an image of a maize leaf to detect diseases and get treatment recommendations.")

# File uploader
uploaded_file = st.file_uploader("Choose a maize leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load and preprocess the image
    image = load_img(uploaded_file, target_size=image_size)
    image_array = img_to_array(image) / 255.0  # Normalize
    image_array = np.expand_dims(image_array, axis=0)

    # Predict using the model
    prediction = model.predict(image_array)
    predicted_class = np.argmax(prediction, axis=1)[0]
    disease_name, recommendation = disease_labels[predicted_class]

    # Display results
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write(f"**Predicted Disease:** {disease_name}")
    st.write(f"**Recommendation:** {recommendation}")

    # Confidence
    confidence = prediction[0][predicted_class] * 100
    st.write(f"**Confidence:** {confidence:.2f}%")
