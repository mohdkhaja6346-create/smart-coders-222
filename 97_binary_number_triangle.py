# Problem 97: Binary number triangle 0 0 1 0 1 0 0 1 0 1 Nested Loops / Inner For Loops - Patterns Alphabet Patterns

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print((i + j + 1) % 2, end=" ")
    print()
