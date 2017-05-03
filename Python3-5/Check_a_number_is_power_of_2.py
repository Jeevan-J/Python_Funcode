#In this python file, we will try to check whether if a given positive number is a power of 2.
#Suppose 'X' is given number, if X = 2 ^ Y (for some Y) then output will be True, Else output will be False. If true, we will also print what is the power.
#Now lets get into the code
num=int(input("please enter a number:")); #Get a positive number as input
if(((num%2)==0)&(num>0)):                 #Check whether the input is even and positive, if not print FALSE
    c=1                                   #Since we want the power value, and minimum power is 1, set a variable to 1 (here c=1)
    while(((num/2)!=1)&(num>=3)):         #here we divide the input by 2 and check if (num is greater than 3 and (num/2) is not equal to 1). if true while loop executes
        num=num/2;                        #we assign (num/2) value to num i.e, we decrease the power by 1.
        c=c+1;                            #since we decrease the power by 1, we increase the count by 1.
    if((num%2)==0):                       #While loop exits when ((num/2) is equal to 1 OR num is less than or equal to 3). If the given input number is power of 2, then last number after while loop will be 2 or else 3,which implies (num%2) should be zero for num =2.
        print("True");                    #print function prints a string - "True"
        print(c);                         #print func prints value stored in 'c'.
    else:
        print("False");
else:
    print("False");
