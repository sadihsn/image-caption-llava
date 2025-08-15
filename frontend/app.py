import streamlit as st
import requests

st.title("Image Caption Generator (LLaVA)")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        try:
            res = requests.post("http://localhost:8000/caption/", files=files)
            res.raise_for_status()
            caption = res.json().get("caption", "Error generating caption.")
        except requests.exceptions.RequestException as e:
            caption = f"Request failed: {e}"

        st.subheader("Caption:")
        st.write(caption)