# Problem 110: Plus (+) pattern     * * * * * * * * * Nested Loops / Inner For Loops - Patterns Advanced Patterns (Nested Logic)

n = int(input("Enter odd size: "))
middle = n // 2

for i in range(n):
    for j in range(n):
        if i == middle or j == middle:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
