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

# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_homeless col as proportion of total homeless population to the state population
homelessness["p_homeless"] = homelessness["total"] / homelessness["state_pop"]

# See the result
print(homelessness)

# COMBINATION
# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"] 

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)