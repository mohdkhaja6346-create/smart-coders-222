# Problem 91: 1-0 alternating triangle 1

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print((i + j) % 2, end=" ")
    print()
