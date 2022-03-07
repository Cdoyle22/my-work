# program that prints out random fruit
#Author:Ciara Doyle

import random
fruits = ['Apple', 'Orange', 'Blueberry', 'Banana', 'Pear']
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit: {}".format(fruit))

