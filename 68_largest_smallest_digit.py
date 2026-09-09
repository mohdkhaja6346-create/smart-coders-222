# Problem 68: Find the largest and smallest digit in a number Find the largest and smallest digit in a number Loops Applied / Mixed Loop Problems

n = abs(int(input("Enter number: ")))
largest = 0
smallest = 9

while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    n //= 10

print("Largest digit =", largest)
print("Smallest digit =", smallest)
