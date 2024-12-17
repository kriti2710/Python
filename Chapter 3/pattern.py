n = int(input("Enter the size: "))

for i in range(n*2-1):
    for j in range(n*2-1):
        if abs(i - (n - 1)) + abs(j - (n - 1)) < n:
            if i == n - 1 and j == n - 1:
                print("a", end=" ")
            elif (i + j) % 2 == 0:
                print("c", end=" ")
            else:
                print("b", end=" ")
        else:
            print(" ", end=" ")
    print()

