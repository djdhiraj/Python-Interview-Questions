# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class First_String(object):

    def __init__(self):
        self.b = ''

    def getString(self):
        self.b = input("Enter any name")

    def getPrint(self):
        print(self.b)


obj = First_String()
obj.getString()
obj.getPrint()
