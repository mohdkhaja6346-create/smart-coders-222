# Problem 8: Read three numbers and check if all three are equal (use && ) Read three numbers and check if all three are equal (use && )

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b and b == c:
    print("All three are equal")
else:
    print("They are not all equal")
