import streamlit as st
import pandas as ps
import requests as r
import snowflake.connector as sc
from urllib.error import URLError

# my function
def get_fruity_data( myfruit ):
  fruityvice_response = r.get("https://fruityvice.com/api/fruit/" + myfruit)
  fruityvice_normalized = ps.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
# function to query snowflake table 
def get_fruit_list():
    with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from fruit_load_list")
      return my_cur.fetchall()
  
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
# ************************************************
#fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
#st.write('The user entered ', fruit_choice)
#fruityvice_response = r.get("https://fruityvice.com/api/fruit/" + fruit_choice)
## st.text(fruityvice_response)
## st.text(fruityvice_response.json()) # just write on screen

## write your own comment -what does the next line do? 
#fruityvice_normalized = ps.json_normalize(fruityvice_response.json())
## write your own comment - what does this do?
#st.dataframe(fruityvice_normalized)
# *************************************************
# move the above to TRY CATCH
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit...")
  else:
    myfruit_data = get_fruity_data(fruit_choice)
    st.dataframe(myfruit_data)
except URLError as e:
  st.error()

# stopall above streamlit execution
#st.stop()

# ******** replaced with function ***
# my_cur = my_cnx.cursor()
## my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_cur.execute("select * from FRUIT_LOAD_LIST")
# my_data_row = my_cur.fetchone()
# st.text("test - Fruit List Data - fetch one:")
# st.text(my_data_row)
# st.header("test - Fruit List Data - fetch 1st in list:")
# st.dataframe(my_data_row)
# ***********************************

st.header("test - Fruit List Data - fetch all:")

# button
if st.button( 'Get List' ):
  # connect to snowflake DB - workshop final part 
  my_cnx = sc.connect(**st.secrets["snowflake"])
  my_data_rows = get_fruit_list()  
  #st.dataframe(my_data_rows)
 
fruit_add = st.text_input('What fruit would you like to add?','jackfruit')
st.write('Thanks for adding ', fruit_add)

my_cur.execute( "insert into FRUIT_LOAD_LIST values ('from st')" )
