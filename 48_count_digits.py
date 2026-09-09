# Problem 48: Count the number of digits in a number Count the number of digits in a number Loops Digit-Based Problems

n = abs(int(input("Enter number: ")))

if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        count += 1
        n //= 10

print("Number of digits =", count)
