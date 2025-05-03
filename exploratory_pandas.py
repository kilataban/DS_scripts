#how to explore a python Data Frame Head
print(df_name.head())

#Explore DataFrame Info
print(df_name.info())

#Understand the shape of the data
print(df_name.shape)

#get summary statistics on the data using describe
#this is good for a numerical overview of numbers
print(df_name.describe())

#how to display the components of a dataframe
print(df_name.values)

print(df_name.columns)

#to check number indexing of rows
print(df_name.index)

#SORTING AND SUBSETTING

#sorting values by column name
df_name.sort_values("column_name")

#sorting values by column name in descending order
df_name.sort_values("column_name", ascending=False)

#sorting values by multiple variables
df_name.sort_values(["column_name_1", "column_name_2"])

#sorting values by multiple variables (Ascending, and Descending)
df_name.sort_values(["column_name_1", "column_name_2"], ascending=[True, False])

#SUBSETTING COLUMNS
df_name["column_name"]

#Subsetting Multiple columns
df_name[["first_column_name", "second_column_name"]]

#Subsetting rows
df_name["column_name"] > 50

#Subsetting based on text data
df_name[df_name["column_name"] == "Text needed"]

#Subsetting the data by date
df_name[df_name["column_name"] < "2025-01-01"]

#Subsetting based on multiple conditions
is_lab = dogs["breed"] == "Labrador"
is_brown = dogs["color"] == "Brown"

#concatenating subset conditions
dogs[is_lab & is_brown]

#Alternative code write for multiple conditions
dogs[ (dogs["breed"] == "Labrador") & (dogs["color"] == "Brown") ]

is_black_or_brown = dogs["color"].isin(["Black", "Brown"])
dogs[is_black_or_brown]

# subsetting rows by filtering and selection
dogs[dogs["height_cm"] > 60]
dogs[dogs["color"] == "tan"]

# filtering for multiple conditions at once using "bitwise and" operator, &
dogs[(dogs["height_cm"] > 60) & (dogs["color"] == "tan")]
