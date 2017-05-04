#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1.
#Example
#Suppose the following inputs are given to the program:
#3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

input_str = input();            # Takes string as input
dimensions=[int(x) for x in input_str.split(',')]; # splits string at comma and add them into list
rowNum=dimensions[0];
colNum=dimensions[1];
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]; # Creates/Initializes a 2-dimensional array of rowNUm x colNum with all values to be 0. [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col; # This loop calculates element value by 'row x col' and writes it to respective element
print (multilist);