# Problem 47: Calculate the sum of first N natural numbers Calculate the sum of first N natural numbers Loops Digit-Based Problems

n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)
