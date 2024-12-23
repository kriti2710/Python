n = int(input("enter your number:"))
for i in range(1,n+1):
    
    print("*"*i)


for i in range(n):
    for j in range(n):
        print("* ", end=" ")
    print()


for i in range(1, 1+n):
    print(" "*(n-i), end= " ")
    print("*"*i)


for i in range(1, n+1):
    print((n+i), end=" ")
    print(" "*i)


for i in range(1, n+1):
    for j in range(n):
        print(i, end=" ")
    print()

for i in range(1,n+1):
    print((str(i) + " ")* (n))



for i in range(n, 0, -1):
    for j in range(n):
        print(i, end=" ")
    print()


n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*", end = "")
    print()

    
    