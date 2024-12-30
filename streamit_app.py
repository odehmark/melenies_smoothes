# Import python packages
import streamlit as st
cnx = st.connection("snowflake")
session = cnx.session()
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Customise Your Smoothie :cup_with_straw:")
st.write(
    """Choose the fruites you want in your custom Smoothie
    """
)

name_on_order  = st.text_input('Name of Smoothie:')
st.write('The name of your smoothie will be', name_on_order )

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list =st.multiselect(
    'Choose up to 5 ingredients:'
     ,my_dataframe
     ,max_selections = 5
)

if ingredients_list:
    ingredients_string =''
    
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen +''

    #st.write( ingredients_string)


# my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
#             values ('""" + ingredients_string + """')"""

my_insert_stmt = """ INSERT INTO smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+ name_on_order +"""')"""

# st.write(my_insert_stmt)
# st.stop()

# st.write(my_insert_stmt)
time_to_insert = st.button('Submit Order')

if time_to_insert:
    session.sql(my_insert_stmt).collect()

#if ingredients_string:
    #session.sql(my_insert_stmt).collect()
    
    # st.success('Your Smoothie is ordered,{NAME_ON_ORDER}!', icon="✅")

if name_on_order:
    st.success(f'Your Smoothie is ordered, {name_on_order}!', icon="✅")
import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response)

