# Problem 70: Check if a number is a perfect number (sum of divisors == number) Check if a number is a perfect number (sum of divisors == number) Loops Applied / Mixed Loop Problems

n = int(input("Enter number: "))
total = 0

for i in range(1, n):
    if n % i == 0:
        total += i

if total == n:
    print("Perfect number")
else:
    print("Not a perfect number")
