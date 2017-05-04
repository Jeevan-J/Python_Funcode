#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
import math      # imports 'math' module which contains various math inbuilt functions
c,h=50,30;       # assigns value to respective variables
value = [];      # creates a list
items=[x for x in input("Please enter values of H separated by comma ',':").split(',')]; # Takes input values from user and separates them at comma and adds them to list 'items'.
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h))))); #Calculates Q for different values of D and stores them in list 'value'

print (','.join(value)); # prints all values of list 'value' separated by comma ','