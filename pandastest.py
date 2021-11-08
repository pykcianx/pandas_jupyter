import pandas as pd
import xml.etree.ElementTree as et

from pandas.core.indexes.base import Index
#from openpyxl import Workbook

file = pd.read_excel('pandasa.xlsx')
#file2 = pd.read_csv('addresses.csv')
#frame = file.iloc[0:4]
#frame2 = file.loc[4, :]

#SELECT ONLY ONE COLUMN
'''
df2 = file.loc[:, 'SAMOZWANCY']
print(df2)
'''


'''
df2 = file.iloc[4, 1]       # [row, column]
print(df2)
'''


#ORDER ROWS
'''
df2=file[file.columns[[1, 0]]]
print(df2)
'''

#COLUMN CHANGE PLACES
'''
#zamiana kolumn
cols = list(file)
cols = [cols[-1]] + cols[:-1]           
df = file[cols]

print(df)
'''
#print(df)
#reversed = file.iloc[::-1]          #w odwrotnej kolejnosci
#reversed[...] reindexes the DataFrame using this new sequence
#print(reversed)
#print(file.head(4))                 #pierwsze x wierszy
#print(file.tail(4))                 #ostatnie x wierszy
#print(file.dtypes)                  #shows datatypes of columns
#df["one"]                           #selecting data frame
#del df["two"]                       #deleting data frame 
#df["one_trunc"] = df["one"][:2]     #insering values from one df to another

'''
loc[row_label, column_label]                    loc gets rows (and/or columns) with particular labels.
iloc[row_position, column_position]             iloc gets rows (and/or columns) at integer locations.

The .loc indexer can also do boolean selection. For instance, if we are interested in finding all the rows wher age is above 30 and return just the food and score columns we can do the following:
df.loc[df['age'] > 30, ['food', 'score']] 


 '''