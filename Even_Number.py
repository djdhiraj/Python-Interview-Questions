# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the
#  number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

b = []
for i in range(1000, 3000):
    a = str(i)
    if (int(a[0]) % 2 == 0) and (int(a[1]) % 2 == 0) and (int(a[2]) % 2 == 0) and (int(a[3]) % 2 == 0):
        b.append(a)
print(",".join(b))

# for three digit numbers 
items = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        items.append(s)
print(",".join(items))
