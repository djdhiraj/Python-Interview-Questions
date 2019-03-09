#Create a program that asks the user for a number and then prints out a list of all the divisors of that number


a = int(input("Enter any number"))
b = []
for i in range(1, a+1):
    if a % i == 0:
        b.append(i)
print(b)


