
import streamlit

streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('ð¥£ Omega 3 & Buleberry oatmeal ')
streamlit.text(' ð¥ kale,spinach & Rocket smoothie')
streamlit.text(' ð Hard-boiled free-range Egg')
streamlit.text('ð¥ðAvocado Toast')
streamlit.header('ðð¥­ Build Your Own Fruit Smoothie ð¥ð')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

