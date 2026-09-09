# Problem 51: Check if a number is a palindrome Check if a number is a palindrome Loops Digit-Based Problems

n = input("Enter number: ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
