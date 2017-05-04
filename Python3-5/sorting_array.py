#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world
items=[x for x in input("Please enter a sequence of words separated by comma:").split(',')]; # Takes user input sequence of words and separates them at comma and adds them to a list
items.sort();   # Assume List is class, then 'sort()' is method of class 'List'. This sort() method sorts the values of list in ascending order.
print (','.join(items)); # Prints values of sorted list separated by comma