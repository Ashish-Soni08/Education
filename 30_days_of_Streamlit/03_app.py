import streamlit as st

# creates a header text for the app
st.header('st.button')

# if the button is clicked, print the following
if st.button('Say hello'): 
     st.write('Why hello there')
else:
     st.write('Goodbye')