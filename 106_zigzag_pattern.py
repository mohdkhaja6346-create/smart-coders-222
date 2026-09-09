# Problem 106: Zigzag pattern * * * * * * * * * Nested Loops / Inner For Loops - Patterns Advanced Patterns (Nested Logic)

n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if i % 2 == 0 and j % 2 == 0:
            print("*", end=" ")
        elif i % 2 == 1 and j == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
