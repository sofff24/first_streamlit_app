import streamlit
import pandas as pd


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



# New section to display fruitvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)



import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# take the json version of the response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# output in the screen as a table
streamlit.dataframe(fruityvice_normalized)



# import snowflake.connector

# # my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cnx = snowflake.connector.connect(
#     account=streamlit.secrets["snowflake"]["account"],
#     user=streamlit.secrets["snowflake"]["user"],
#     password=streamlit.secrets["snowflake"]["password"],
#     warehouse="PC_RIVERY_WH"  # Specify the warehouse here
# )

# my_cur = my_cnx.cursor()
# # my_cur.execute("USE WAREHOUSE PC_RIVERY_WH SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
# my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
# my_data_rows = my_cur.fetchall()
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_rows)







