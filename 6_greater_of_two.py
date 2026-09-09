# Problem 6: Read two numbers and print which is greater (use relational operators) Read two numbers and print which is greater (use relational operators)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Greater =", a)
elif b > a:
    print("Greater =", b)
else:
    print("Both are equal")
