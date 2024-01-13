import pandas as pd

orders=pd.read_table('http://bit.ly/chiporders')
print(orders.head())
print('\n')

#To capitalise the item names:
print(orders.item_name.str.upper())
print('\n')

#To check whether a particular series contains an item:
print(orders.item_name.str.contains('Chicken'))
print('\n') 

#To get only a list of orders that contain the word Salsa in their name:
print(orders[orders.item_name.str.contains('Salsa')])
print('\n')

#To remove the [...] square brackets present under the choice_description column:
print(orders.choice_description.str.replace('[','').str.replace(']',''))
print('\n')
