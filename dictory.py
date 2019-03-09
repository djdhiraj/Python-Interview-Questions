# With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
8

a = int(input("Enter any number"))
b = dict()
for i in range(1, a+1):
    b[i] = i*i
print(b)

