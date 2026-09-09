# Problem 67: Check if a number is an Armstrong number (generalized for any digits) Check if a number is an Armstrong number (generalized for any digits) Loops Applied / Mixed Loop Problems

n = int(input("Enter number: "))
original = n
digits = len(str(abs(n)))
total = 0

while n > 0:
    digit = n % 10
    total += digit ** digits
    n //= 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
