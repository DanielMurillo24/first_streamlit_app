import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')


streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, spinach & Rocket Smootthie')
streamlit.text('🐔 Hard-boile Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toats')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
