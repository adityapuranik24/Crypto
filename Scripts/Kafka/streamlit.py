import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello I am streamlit function!")
json = {
    "a": "Aditya",
    "b": "Puranik"
}
st.text("# Header 1")
st.json(json)

st.markdown('# Hello World')
st.markdown("1. Item 1")
st.markdown("2. Item 2")
st.write({
    "a": "Aditya",
    "b": "Puranik"
})
st.write("## Heading 2")

# Writing code without any st methods
"""
# My first app
Here's our first attempt at using data to create a table:
"""


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

#static table
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

#Sample line chart

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


#widget
x = st.slider('x')  #  this is a widget
st.write(x, 'squared is', x * x)


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option