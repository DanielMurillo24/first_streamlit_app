import streamlit
import pandas
import requests

streamlit.title("My Mom's New Healthy Diner")


streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, spinach & Rocket Smootthie')
streamlit.text('🐔 Hard-boile Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toats')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# New Section to Display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

#Take the json version of the response and normalize it
fruityvice_normalized = pandas.jason_normalize(fruityvice_response.json())
#Output it the screen as a table
streamlit.dataframe(fruityvice_normalized)
