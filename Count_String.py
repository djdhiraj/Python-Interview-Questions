a = input("Enter the number you want")

b = sum(c.isalpha() for c in a)
c = sum(c.isdigit() for c in a)
d = sum(c.isspace() for c in a)
print("Latter:",b)
print("Digits:",c)

print("Space:",d)

# Another way to same problem
s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print ("DIGITS", d["DIGITS"])