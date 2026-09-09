# Problem 50: Reverse a number Reverse a number Loops Digit-Based Problems

n = int(input("Enter number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reverse =", reverse)
