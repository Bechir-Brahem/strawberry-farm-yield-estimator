import streamlit as st
import numpy as np
from PIL import Image
from detection.detect import detect_object


def main():
    st.title("Object detection with YOLOv5")
    ret=upload_image_ui()
    if ret=='ok':
        detection,ripe,unripe = detect_object()
        st.text('detection')
        st.image(detection)
        st.header(f'number of ripe strawberries: {ripe}')
        st.header(f'number of unripe strawberries: {unripe}')
        estim= 0 if ripe==0 else ripe/(ripe+unripe)
        st.header(f'strawberry farm yield estimation: {round(estim,2)*100}%')

def upload_image_ui():
    uploaded_image = st.file_uploader("Please choose an image file", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        try:
            print(uploaded_image)
            image = Image.open(uploaded_image)
            image.save('source.jpg')
            return 'ok'
        except Exception:
            st.error("Error: Invalid image")

if __name__ == '__main__':
    main()
