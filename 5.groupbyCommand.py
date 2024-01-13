import pandas as pd

drinks=pd.read_csv('http://bit.ly/drinksbycountry')

#To find the mean of beer servings:
print(drinks.beer_servings.mean())
print('\n')

#To find the mean of beer servings per continent,we can use the group by command:
print(drinks.groupby('continent').beer_servings.mean())
print('\n')

#Other than mean,we can also find other values like minimum, maximum etc
#We can also get all of these printed together through a single command 'agg'

print(drinks.groupby('continent').beer_servings.agg(['count','min','max','mean']))
print('\n')

#We can also get the mean,min etc values across all the columns at once:
print(drinks.groupby('continent').mean())
print('\n')

