# A program that makes a list that has 10 random numbers (20000-800000)


import numpy as np

minSalary = 20000
MaxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint(minSalary, MaxSalary, numberOfEntries)

print(salaries)
