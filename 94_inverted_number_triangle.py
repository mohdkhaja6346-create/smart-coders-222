# Problem 94: Inverted number triangle 1 2 3 4

n = int(input("Enter rows: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
