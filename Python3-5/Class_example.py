# In this we will define a class and we will see how to get an instance or object from the class
class InputOutString(object):      # Define a class with name 'InputOutString'
    def __init__(self):            # Predefined method '__init__'
        self.s = "" ;              # Create a variable 's' with empty string.

    def getString(self):           # defines a method 'getString()' with no arguments
        self.s = input();          # Takes user input string and assigns it to variable 's'

    def printString(self):         # defines a method 'printString()' with no arguments
        print (self.s.upper());    # Prints the string in 's' in uppercase letters

strObj = InputOutString()          # Creates an object "strObj" of class "InputOutString"
strObj.getString()                 # Asks user for an input
strObj.printString()               # prints the user input string in Uppercase Letters
print(strObj.s)                    # prints the user input string as it is. i have added this line just to show you that we can access variables in class also.

# If a class is defined with different methods, we can those methods on objects without knowning the source code of class methods.
