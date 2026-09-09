# Problem 108: Right arrow pattern * * * * * * * * * * * Nested Loops / Inner For Loops - Patterns Advanced Patterns (Nested Logic)

n = int(input("Enter size: "))

for i in range(n):
    if i < n // 2:
        stars = i + 1
    elif i == n // 2:
        stars = n
    else:
        stars = n - i

    print("* " * stars)
