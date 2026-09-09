# Problem 73: Read numbers until user enters −1, print the count and average Read numbers until user enters −1, print the count and average Loops Applied / Mixed Loop Problems

total = 0
count = 0

while True:
    n = float(input("Enter number (-1 to stop): "))
    if n == -1:
        break
    total += n
    count += 1

if count > 0:
    print("Count =", count)
    print("Average =", total / count)
else:
    print("No numbers entered")
