# Factorial funtion in python

a = int(input("enter any number"))


def fac(i):
    if i == 0:
        return 1
    else:
        return i * fac(i - 1)


c = fac(a)
print(c)
