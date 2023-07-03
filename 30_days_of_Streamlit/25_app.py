import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)


### The above 2 custom functions will be called upon as soon as a numerical value is entered into the number box created using the st.number_input command. 
### Notice how the on_change option specifies the 2 custom functions lbs_to_kg and kg_to_lbs).
### In a nutshell, upon entering a number into the st.number_input box the number is converted by these custom functions.
### Finally, the weight values in kg and lbs units as stored in the session state as st.session_state.kg and st.session_state.lbs will be printed out via st.write
