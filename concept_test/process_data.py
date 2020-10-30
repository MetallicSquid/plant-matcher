# Script to collect the data described in the 'Companion Plants' wikipedia page
import pandas as pd
from numpy import nan

# Scrape the tables and convert them to a dataframe
data_list = pd.read_html(r"https://en.wikipedia.org/wiki/List_of_companion_plants", header=1, na_values="")
dataframe = pd.DataFrame()
for i in range(5):
    dataframe =pd.concat([dataframe, data_list[i]])
dataframe.fillna('', inplace=True)

# Remove the duplicated headers
dataframe = dataframe.drop_duplicates()
dataframe = dataframe.reset_index(drop=True)
dataframe = dataframe.drop(5)
dataframe = dataframe.reset_index(drop=True)

# Remove (or replace) the unwanted patterns and columns
for column in dataframe.columns.values:
    dataframe[column] = dataframe[column].str.replace(r"\[\d+\]", "")
    dataframe[column] = dataframe[column].str.replace(r"\[\bcitation needed\b\]", "")
    dataframe[column] = dataframe[column].str.replace(r"e.g.", "")
    dataframe[column] = dataframe[column].str.replace(r"(", ",")
    dataframe[column] = dataframe[column].str.replace(r")", "")
    dataframe[column] = dataframe[column].str.replace(r", ", ",")
    dataframe[column] = dataframe[column].str.replace(r"&", ",")
    dataframe[column] = dataframe[column].str.replace(r"and", ",")
    dataframe[column] = dataframe[column].str.replace(r".", "")
dataframe = dataframe.drop(["Scientific name", "Comments"], axis=1)

# Create comparison dictionaries for the relevant columns
'''
    *   Split cell into list
    *   Iterate over list
    |--->   Check whether individual item has a wikipedia page
    |--->   Find relevant information on the item
    |--->   Assign a key-value pair in the relevant dictionary for the item
'''
help_dict = {}
helped_by_dict = {}
attract_dict = {}
repel_dict = {}
avoid_dict = {}

# 'Helps' column
for item in dataframe.Helps:
    # Split cell into list
    item.strip()
    current_list = []
    if item != '':
        current_list = item.split(",")
    for element in current_list:
        pass
        # Run search function on `element`


# 'Helped by' column
# 'Attracts' column
# 'Repels' column
# 'Avoids' column

dataframe.to_csv("temp.csv")
