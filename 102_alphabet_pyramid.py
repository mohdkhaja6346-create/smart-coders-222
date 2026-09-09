# Problem 102: Alphabet pyramid (centered)       A A B A A B C B A A B C D C B A Nested Loops / Inner For Loops - Patterns Advanced Patterns (Nested Logic)

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")

    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end=" ")

    print()
