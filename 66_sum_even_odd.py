# Problem 66: Find the sum of even and odd numbers separately from 1 to N Find the sum of even and odd numbers separately from 1 to N Loops Applied / Mixed Loop Problems

n = int(input("Enter N: "))
even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Even sum =", even_sum)
print("Odd sum =", odd_sum)
