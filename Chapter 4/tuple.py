t = (1,2,3,3,3,4) #tuple is immutable , you cannot its value
# print(type(t))

# no = t.count(3)
# print(no)

t2 = ( 5,6,7,2,7)
concatenate = t + t2
print(concatenate)

# print(t.index(2))

Repetition = t2 * 3
print(Repetition)

membership = (2 in t)
print(membership)

print(len(t2))

print(min(t))
print(max(t))

for item in (1,2,3,4):
    print(item)