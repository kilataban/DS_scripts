# Selective print
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
for lab, row in brics.iterrows():
    print(lab + ": " + row["capital"])


#Add columns using pandas data structures
import pandas as pd
brics = pd.read_csv("brics.csv", index_col= 0)
for lab, row in brics.iterrows():
    brics.loc[lab, "name_length"] = len(row["country"])
print(brics)


#optimised for large datasets -> apply
import pandas as pd
brics = pd.read_csv("brics.csv", index_col = 0)
brics["name_length"] = brics["country"].apply(len)
print(brics)

#to create an uppercase label column
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
cars["COUNTRY"] = cars["country"].apply(str.upper)


#Iterrate over different labels and rows
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

for lab, row in cars.iterrows():
    print(lab)
    print(row)

#Adapt for loop
for lab, row in cars.iterrows():
    print(lab + ": " + str(row['cars_per_cap']))

#Uppercase a variable
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()