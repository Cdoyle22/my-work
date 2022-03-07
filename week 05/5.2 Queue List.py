# Program that puts 10 random numbers into a list, then output all the values in the list
# then take the numbers from the list one at a time, print it and the current numbers still in the list
# Author: Ciara Doyle

import random
RandomNumbers = []
numberofNumbers = 10
rangeTo = 100

for n in range(0,  numberofNumbers):
    RandomNumbers.append(random.randint(0,rangeTo))

print("RandomNumbers is []".format(RandomNumbers))

while len(RandomNumbers) !=0:
    currentNumber = RandomNumbers.pop(0)
    print ("current Number is {} and the RandomNumbers is {}".format(currentNumber, RandomNumbers))

print ("the queue is now empty")
