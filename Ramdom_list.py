import random
import timeit

b=[]
for i in range(1,11):
    a = random.randint(4,101)
    b.append(a)
print(b)
c=[]
for i in range(1,9):
    a = random.randint(4,101)
    c.append(a)
print(c)

d=[i for i, j in zip(b, c) if i == j]
print(d)

# d=[]
# for i in b:
#     for j in c:
#         if i==j:
#             break
#         else:
#             d.append(i)
#
# print(d)