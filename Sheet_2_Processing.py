import pandas as pd 
import numpy as np 

df = pd.read_excel("DATA SET.xlsx", sheet_name="ticket")
df = df.sort_values(by='saledate')

df['Popcorn_Price'] = None 
df['Popcorn_Price'] = df['popcorn'].apply(lambda x:0 if x == 'Không' else None)

# Function to pop elements from a column and return them in a list
def turn_series_to_list(df, col):
    popped_elements = []

    for index, row in df.iterrows():
        if row[col]:
            popped_element = row[col]
            popped_elements.append(popped_element)

    df.pop(col)

    return popped_elements

# Call the function with your DataFrame and column name
total_popped_elements_list = turn_series_to_list(df, 'total')
date_popped_elements_list = turn_series_to_list(df, 'date')
film_popped_elements_list = turn_series_to_list(df, 'film')
slot_popped_elements_list = turn_series_to_list(df, 'slot type')
popcorn_popped_elements_lists = turn_series_to_list(df, 'popcorn')

df2['Popcorn_Price'] = None 
df2['Popcorn_Price'] = df2['popcorn'].apply(lambda x:0 if x == 'Không' else None)
