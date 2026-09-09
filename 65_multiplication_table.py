# Problem 65: Print the multiplication table of a given number Print the multiplication table of a given number Loops Applied / Mixed Loop Problems

n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
