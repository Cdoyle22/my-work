# Program that keeps reading numbers until the user enters a 0 and then print out each of the numbers entered and the average of them.
# Author: Ciara Doyle

numbers = []

number = int(input("enter number (0 to quit): "))

while number !=0:
    numbers.append(number)

    number = int(input("enter another (0 to quit) :"))

for value in numbers:
    print (value)

average = float(sum(numbers)) / len(numbers)
print ("The average is {}".format(average))

