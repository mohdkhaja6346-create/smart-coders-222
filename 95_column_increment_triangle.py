# Problem 95: Column-wise incrementing 1

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
