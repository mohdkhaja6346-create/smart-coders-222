# Problem 76: Count Vowels: Count the number of vowels in a string using recursion. Count Vowels: Count the number of vowels in a string using recursion.

def count_vowels(s):
    if s == "":
        return 0
    if s[0].lower() in "aeiou":
        return 1 + count_vowels(s[1:])
    return count_vowels(s[1:])

s = input("Enter string: ")
print("Vowels =", count_vowels(s))
