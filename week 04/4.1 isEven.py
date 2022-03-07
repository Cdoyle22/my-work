# program that asks the user to enter in a number, and the program will tell the user if the number is even or odd. 
# Author: Ciara Doyle

x = int(input("Enter a number: "))

if (x % 2) == 0:
    print ("{} is an even number".format(x))
else:
    print("{} is an odd number".format(x))
    
