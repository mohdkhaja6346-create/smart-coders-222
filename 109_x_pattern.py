# Problem 109: X pattern *     * *     * * *     * *     * Nested Loops / Inner For Loops - Patterns Advanced Patterns (Nested Logic)

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
