# Problem 15: Count Set Bits

n = int(input("Enter number: "))
count = 0

while n > 0:
    count += n & 1
    n = n >> 1

print("Set bits =", count)
