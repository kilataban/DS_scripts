
import numpy as np
np.random.rand()

# you can set your own seed to ensure reproducibility, 123 is an example seed

np.random.rand(123)

# this is called a psuedo random number
np.random.seed(123)
coin = np.random.randint(0,2)

if coin == 0:
    print("heads")
else:
    print("tails")


# Generate and print random float
print(np.random.rand())


# Random Steps: Sequential progressive random number selections
import numpy as np
np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0,2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")

print(outcomes)


# Random Walk: Sequential progressive random number selections and tracking
import numpy as np
np.random.seed(123)
tails = [0]

for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)
print(tails)