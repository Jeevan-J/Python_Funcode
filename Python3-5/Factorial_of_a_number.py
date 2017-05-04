#Write a program which can compute the factorial of a given numbers.
#We will first define a function
def fact(x):                 #Define a function named 'fact()'
    if x == 0:               #We directly return 1 if input number is 0.
        return 1 ;
    return x * fact(x - 1);  # We return 'number * fact(number - 1)'. We are calling the same function again in its own function, This is called Recursive Function

x=int(input("Please enter a number:"));
print fact(x);
