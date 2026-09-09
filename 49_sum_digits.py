# Problem 49: Find the sum of digits of a number Find the sum of digits of a number Loops Digit-Based Problems

n = abs(int(input("Enter number: ")))
total = 0

while n > 0:
    total += n % 10
    n //= 10

print("Sum of digits =", total)
