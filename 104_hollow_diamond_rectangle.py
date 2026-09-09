# Problem 104: Hollow diamond inside rectangle * * * * * * * * * *   * * * * *       * * *           * * *       * * * * *   * * * * * * * * * * Nested Loops / Inner For Loops - Patterns Advanced Patterns (Nested Logic)

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
