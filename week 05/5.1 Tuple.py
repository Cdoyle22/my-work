# Create a tuple that stores the month of the year, from that tuple create another tuple with just the summer months(May, June, July)
# print out summer months one at a time
# Author: Ciara Doyle

MonthsOfYear = ("January", 
                    "February", 
                    "March", 
                    "April", 
                    "May", 
                    "June", 
                    "July", 
                    "August", 
                    "September", 
                    "October", 
                    "November", 
                    "December")

summer = MonthsOfYear[4:7]
for month in summer:
    print(month)
