# Problem 72: Convert binary to decimal Convert binary to decimal Loops Applied / Mixed Loop Problems

binary = input("Enter binary number: ")
decimal = 0

for digit in binary:
    decimal = decimal * 2 + int(digit)

print("Decimal =", decimal)
