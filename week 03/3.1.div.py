#A program that reads in two numbers and divides the first one by the second and give the integer result and the remainder
#Author: Ciara Doyle

x=int(input("Enter first number: "))
y=int(input("Enter the number you want to divide by: "))
answer= (x//y)
remainder = x%y

print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))
