# Problem 69: Print all factors / divisors of a number Print all factors / divisors of a number Loops Applied / Mixed Loop Problems

n = int(input("Enter number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
