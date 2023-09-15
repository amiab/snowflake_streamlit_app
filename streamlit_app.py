import streamlit as st
import pandas as ps

st.title( "Snowflake - ❄️ -" )
st.header( "Data Application Builders" )
st.text( "Workshop - 15/09/2023" )
st.text( "*************************************" )

st.header('Breakfast Menu')
st.text('🥣Omega 3 & Blueberry Oatmeal')
st.text('🥗Kale, Spinach & Rocket Smoothie')
st.text('🐔Hard-Boiled Free-Range Egg')
st.text('🥑🍞Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = ps.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# list picker  
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
st.dataframe(my_fruit_list)
