#in this file we have find whether a given input positive number is a power of 3 or not.
#Similar to the Check_a_number_is_power_of_2.py code, this code also follows same algorithm.
num=int(input("please enter a number:"));
if(((num%3)==0)&(num>0)):
    c=1
    while(((num/3)!=1)&(num>=5)):
        num=num/3;
        c=c+1
    if((num%3)==0):
        print("True");
        print(c);
    else:
        print("False");
else:
    print("False");
