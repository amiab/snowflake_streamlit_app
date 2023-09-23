import streamlit as st
import pandas as ps
import requests as r
import snowflake.connector as sc

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
fruits_to_show = my_fruit_list.loc[fruits_selected] 

# Display the table on the page.
st.dataframe(fruits_to_show) 

# api call - workshop part 2
st.header("Workshop part #2 - Fruityvice!")

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

fruityvice_response = r.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# st.text(fruityvice_response)
# st.text(fruityvice_response.json()) # just write on screen

# write your own comment -what does the next line do? 
fruityvice_normalized = ps.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)

# connect to snowflake DB - workshop final part 
y_cnx = sc.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)
