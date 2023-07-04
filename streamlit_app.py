import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') # Choose the Fruit Name Column as the Index



streamlit.title("My Mom's New Healthy Diner")

streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

 # Let's put a pick list here so they can pick the fruit they want to include   -- # Choose a Few Fruits to Set a Good Example 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries']) #here avocado and strawberries will always appear as default
fruits_to_show = my_fruit_list.loc[fruits_selected] # make the table smaller depending on the selection of fruits

# Display the table on the page.
streamlit.dataframe(fruits_to_show)



#############################################

# create the repeateable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
 fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
 return fruityvice_normalized


# New section to display fruitvice api response
streamlit.header("Fruityvice Fruit Advice!")

## new ##
try: 
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
  streamlit.error("Please a fruit to get information.")
 else:
   back_from_function = get_fruityvice_data(fruit_choice)
   streamlit.dataframe(back_from_function)

except URLError as e:
 streamlit.error()


##########################################
# old #
# streamlit.stop()

# my_cnx = snowflake.connector.connect(
#     account=streamlit.secrets["snowflake"]["account"],
#     user=streamlit.secrets["snowflake"]["user"],
#     password=streamlit.secrets["snowflake"]["password"],
#     warehouse="PC_RIVERY_WH"  # Specify the warehouse here
# )

# my_cur = my_cnx.cursor()



# my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
# my_data_rows = my_cur.fetchall()
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_rows)


# add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
# streamlit.write('Thanks for adding ', add_my_fruit)



######################################
# new #
streamlit.header("The fruit load list contains:")
# Snowflake-related functions
def get_fruit_list():
 with my_cnx.cursor() as my_cur:
  my_cur = snowflake.connector.connect(
    account=streamlit.secrets["snowflake"]["account"],
    user=streamlit.secrets["snowflake"]["user"],
    password=streamlit.secrets["snowflake"]["password"],
    warehouse="PC_RIVERY_WH")
  my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
 return my_cur.fetchall()


# Add a button to load the fruit
if streamlit.button('Get Fruit Load List:')
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 my_data_rows = get_fruit_list()
 streamlit.dataframe(my_data_rows)


#############################3

# this will not work correctly, but just go with it for now
# my_cur = my_cnx.cursor()
# my_cur.execute("insert into fruit_load_list values ('from streamlit')")



