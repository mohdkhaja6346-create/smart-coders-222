# Problem 96: Reverse number triangle 4 3 2 1

n = int(input("Enter rows: "))

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
