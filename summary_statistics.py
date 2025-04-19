# Aggregating data from summary stats

# Summarising numerical data

# 1. Mean
dogs["height_cm"].mean()

# Other methods of summary include
.median()  .mode() 
.min()     .max()
.var()     .std()
.sum()
.quantile()


# summary dates example
dogs["date_of_birth"].min()

dogs["date_of_birth"].max()

# The .agg() method
# .agg() does a full aggregation
def pct30(column):
    return column.quantile(0.3)
# this yields the 30th percentile

dogs["weight_kg"].agg(pct30)

# agg can be used on multiple columns
dogs[["weight_kg", "height _cm"]].agg(pct30)

# MULTIPLE SUMMARIES
def pct40(column):
    return column.quantile(0.4)

# this yields the fortieth percentile
dogs["weight_kg"].agg([pct30, pct40])


# CUMULATIVE SUM
dogs["weight_kg"].cumsum()

# OTHER CUMULATIVE STATISTICS METHODS
.cummax()
.cummin()
.cumprod()