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
my_fruit_list = my_fruit_list.set_index('Fruit')

# list picker  
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

if (fruits_selected != null)
{
  fruits_to_show = my_fruit_list.loc[fruits_selected] 
}
else
{
  fruits_to_show = my_fruit_list
}

# Display the table on the page.
st.dataframe(fruits_to_show)
