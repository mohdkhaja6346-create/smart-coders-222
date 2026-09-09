# Problem 92: Pascal's triangle       1

n = int(input("Enter rows: "))

for i in range(n):
    value = 1
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1) if j < i else 1
    print()
