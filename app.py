import streamlit as st
import helper
import pickle

model = pickle.load(open('rf_model.pkl', 'rb'))

st.set_page_config(page_title="Duplicate Question Pair Finder", page_icon=":mag_right:", layout="wide")

st.title("Duplicate Question Pair Finder")
st.write("Enter two questions below to check if they are duplicates.")

col1, col2 = st.columns(2)

with col1:
    q1 = st.text_area("Enter question 1", height=150, placeholder="Type question 1 here...")

with col2:
    q2 = st.text_area("Enter question 2", height=150, placeholder="Type question 2 here...")

st.write("\n")

if st.button('Find'):
    if q1 and q2:
    
        query = helper.query_point_creator(q1, q2)
        result = model.predict(query)[0]

    
        if result:
            st.success('The questions are **duplicates**.')
        else:
            st.warning('The questions are **not duplicates**.')
    else:
        st.error('Please enter both questions.')
