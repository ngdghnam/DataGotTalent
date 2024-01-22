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
popcorn_popped_elements_list = turn_series_to_list(df, 'popcorn')
customer_popped_list = turn_series_to_list(df, 'customerid')
time_popped_list = turn_series_to_list(df, 'time')

# turn them into array 
total_popped_arr = np.array(total_popped_elements_list)
date_popped_arr = np.array(date_popped_elements_list)
film_popped_arr = np.array(film_popped_elements_list)
slot_popped_arr = np.array(slot_popped_elements_list)
popcorn_popped_arr = np.array(popcorn_popped_elements_list)
customer_popped_arr = np.array(customer_popped_list)
time_popped_arr = np.array(time_popped_list)

for i in range(len(date_popped_arr)):
    if customer_popped_arr[i] == customer_popped_arr[i+1] and date_popped_arr[i] == date_popped_arr[i+1] and time_popped_arr[i] == time_popped_arr[i+1] and film_popped_arr[i] == film_popped_arr[i+1]:  
        if popcorn_popped_arr[i] == 'Không':
            pass 
        elif popcorn_popped_arr[i] == 'Có':
            pass
        else:
            pass
        pass 

