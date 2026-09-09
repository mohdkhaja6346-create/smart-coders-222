# Problem 38: Armstrong 3 Digit

n = int(input("Enter 3-digit number: "))
original = n
total = 0

while n > 0:
    digit = n % 10
    total += digit ** 3
    n //= 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
