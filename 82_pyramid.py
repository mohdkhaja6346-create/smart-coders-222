# Problem 82: Pyramid

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
