# Subsetting data categoricaly can involve the or operator or | to select rows from multiple categories


#use .isin() method to tackle the problem of writing unnecessarily long statements

colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]

# New columns data manipulation with pandas
dogs["height_m"] = dogs["height_cm"] / 100
print(dogs)

#testing bmi function with dogs dataframe
dogs["bmi"] = dogs["weight_kg"] / dogs["height_m"] ** 2
print(dogs.head())

# multiple manipulations with pandas
bmi_lt_100 = dogs[dogs["bmi"] < 100]
bmi_lt_100_height = bmi_lt_100.sort_values("height_cm", ascending=False)
bmi_lt_100_height[["name", "height_cm", "bmi"]]

#It is possible add new columns to data as well
# These operations are called TRANSFORMING, MUTATING, AND FEATURE ENGINEERING

