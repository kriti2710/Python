# sqaure pattern
n=int(input("enter the number: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*", end= " ")
#     print()


# '''
# *
# * *
# * * *
# * * * * 
# * * * * *
# '''
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()


# '''
# * * * * *
# * * * * 
# * * *
# * *
# *
# '''
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


for i in range(1, 6):
    for j in range(1, i+1): #(1, (1 2))
        print(j, end=" ")
    print()

for i in range(n, 0 , -1):
    for j in range(1, i+1):
        print(j, end= " ")
    print()

for i in range(n, 0 , -1):
    for j in range(i, 0, -1):
        print(j, end= " ")
    print()


for i in range(1, n+1):
    for i in range(1,i+1):
        print("*", end=" ")
    print()


for i in range(1, n+1):
    print(" "* (n-i), end=" ")
    print("*"* (2*i-1), end = " ")
    print()


for i in range(1, n+1):
    print(" "*(n-i))
    print("*"* i, end=" ")
  
print("\n")

for i in range(1, n+1):
    print(" "*(n-i), end=" ")
    print("*"* i, end=" ")
    print()

for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"* n, end= "")
    else:
        print("*", end="")
        print(" "*(n-2), end= "")
        print("*", end="")
    print()