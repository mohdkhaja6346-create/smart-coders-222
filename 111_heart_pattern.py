# Problem 111: Heart shape pattern  *     * * * * * * * * * * * * * * * * * * * * * * * * * Nested Loops / Inner For Loops - Patterns Advanced Patterns (Nested Logic)

n = int(input("Enter size: "))

for i in range(n // 2, n, 2):
    print(" " * ((n - i) // 2) + "*" * i + " " * (n - i) + "*" * i)

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
