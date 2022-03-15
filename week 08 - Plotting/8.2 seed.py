# A program that makes a list that has 10 random numbers (20000-800000)
# seed the random  numbers generator


import numpy as np

minSalary = 20000
MaxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint(minSalary, MaxSalary, numberOfEntries)
np.random.seed(1)

salariesPlus = salaries + 5000
#make another array of numbers that has the salaries plus 5000

salariesMult = salaries * 1.05
print (salariesMult)
#increase all the salaries by 5%

print (salariesPlus)
print (salaries)