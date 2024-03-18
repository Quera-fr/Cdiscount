import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    image = st.image(picture)


# Save the image
st.button("Save image", picture)