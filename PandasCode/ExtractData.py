# import Pandas

import pandas as pd

# using read_csv()

person_data = pd.read_csv("data.csv", header=0, sep=",")

## show data

#print(person_data)


## when the csv file its so long, you can use the head() to show x amount of data

#print(person_data.head())


## delete data using dropna()

person_data.dropna(axis=0, inplace=True)

print(person_data)





