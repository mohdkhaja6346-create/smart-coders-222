# Problem 75: Palindrome Check: Check whether a string is a palindrome using recursion Palindrome Check: Check whether a string is a palindrome using recursion

def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

s = input("Enter string: ")

if palindrome(s):
    print("Palindrome")
else:
    print("Not palindrome")
