#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
values=input("Please enter some numbers separated by comma ',':");
l=values.split(",");      #String data type has a method 'split', which splits string by given letter and convert it into a list
t=tuple(l)                # 'tuple' is method that converts list to tuple
print (l);                # Prints list
print (t);                # Prints tuple


# For example,Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')
