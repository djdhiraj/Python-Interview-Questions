a = [1, 2, 12, 90, 6, 7, 8, 9, 3, 13, 31, 86]
b = []
for i in a:
    if i < 20:
        b.append(i)
print(a)
print(len(a))
print(b)
b.sort(reverse=False)
print(b)
