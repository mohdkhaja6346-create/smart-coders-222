# Problem 53: Product of Digits: Find the product of all digits of a number using recursion. Product of Digits: Find the product of all digits of a number using recursion. Loops Digit-Based Problems

def product_digits(n):
    if n < 10:
        return n
    return (n % 10) * product_digits(n // 10)

n = abs(int(input("Enter number: ")))
print("Product of digits =", product_digits(n))
