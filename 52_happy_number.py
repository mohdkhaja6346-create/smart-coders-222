# Problem 52: Happy Number: Repeatedly replace a number with the sum of the squares of its digits. Determine whether it eventually reaches 1. Happy Number: Repeatedly replace a number with the sum of the squares of its digits. Determine whether it eventually reaches 1. Loops Digit-Based Problems

n = int(input("Enter number: "))
seen = set()

while n != 1 and n not in seen:
    seen.add(n)
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    n = total

if n == 1:
    print("Happy number")
else:
    print("Not a happy number")
