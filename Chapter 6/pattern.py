# n = int(input())

# for i in range (1, 1+n):
#     for j in range (1, n*2):
#         if((i+j)>=(n+1) and (j-i)<= (n)):
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()



# for i in range(1, n+1):
#     print(" " * (n-i), end = " " )
#     print("*" * i)

# for i in range(1, n+1):
#     print(" "*(n-i) + )


n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(64+(n-j+1)),end = " ")
    print()