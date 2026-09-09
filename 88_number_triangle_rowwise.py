# Problem 88: Number triangle (row-wise) 1

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
