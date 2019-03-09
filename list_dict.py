
# Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:

a = input("Enter the number")

b = a.split(",")
print(b)
c = tuple(b)
print(c)