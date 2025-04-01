#to explore a python Data Frame Head
print(df_name.head())

#Explore DataFrame Info
print(df_name.info())

#Understand the shape of the data
print(df_name.shape)

#get summary statistics on the data using describe
#this is good for a numerical overview of numbers
print(df_name.describe())

#to display the components of a dataframe
print(df_name.values)

print(df_name.columns)

#to check number indexing of rows
print(df_name.index)

#SORTING AND SUBSETTING

#sorting values by column name
df_name.sort_values("column_name")

#sorting values in descending order
df_name.sort_values("column_name", ascending=False)

#sorting values by multiple variables
df_name.sort_values(["column_name_1", "column_name_2"])

#sorting values by multiple variables (Ascending, and Descending)
df_name.sort_values(["column_name_1", "column_name_2"], ascending=[True, False])