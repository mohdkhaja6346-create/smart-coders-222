# Problem 101: Right-aligned alphabet triangle       A A B A B C A B C D Nested Loops / Inner For Loops - Patterns Alphabet Patterns

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
