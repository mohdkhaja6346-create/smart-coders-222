# Problem 12: 13  14   5

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a ^ b
b = a ^ b
a = a ^ b

print("After swap:")
print("a =", a)
print("b =", b)
