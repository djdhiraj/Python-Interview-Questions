# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9


a = input("enter any string ")

b = sum(c.islower() for c in a)
c = sum( c.isupper() for c in a )
print("Upper letter",c)
print("Lower Latter",b)

# Another way to solve some problem

s = raw_input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print( "UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])