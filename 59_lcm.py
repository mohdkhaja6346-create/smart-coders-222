# Problem 59: Lcm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = abs(a)
y = abs(b)

while y != 0:
    x, y = y, x % y

gcd = x
lcm = abs(a * b) // gcd if gcd != 0 else 0

print("LCM =", lcm)
