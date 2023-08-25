import streamlit as st
import pandas as pd
import numpy as np

if not "a" in st.session_state:
    st.session_state['a'] = 0

# st.markdown(''' # This is my title''')

# st.markdown("""<h1> BIG TITLE </h1>""", unsafe_allow_html=True)

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

def f():
    st.session_state['a'] += 1

st.button('Hit me',on_click=f)


st.write(st.session_state['a'])


# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
#line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
#head_df = df.head(line_count)

#head_df
