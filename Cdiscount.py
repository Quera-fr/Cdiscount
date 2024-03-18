import streamlit as st
from utiles import get_all_products

# Title
st.title("Scraping Cdiscount")


input_user = st.text_input('Enter a product', 'Iphone 12')

st.write('You entered:', input_user)

# Checkbox
if st.checkbox('I agree with the terms and conditions'):
    if st.button('Collect data'):
        dict_product = get_all_products(input_user)
        st.write(dict_product)
        st.write('Great!')