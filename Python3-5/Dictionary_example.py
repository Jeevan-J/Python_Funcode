#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
n=int(input("Please enter a number"));  # takes an integer from user
d=dict();                               # Creates an empty dictionary
for i in range(1,n+1):                  # Runs loop for n-times with 'i' varying from 1 to n.
    d[i]=i*i;                           # Maps every element to its square of index.
print (d);                              # Prints dictionary 'd'

# For example, If input is 8, then output should look like,
# {1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64}
