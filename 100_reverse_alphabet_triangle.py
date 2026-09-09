# Problem 100: Reverse alphabet triangle A B C D A B C A B A Nested Loops / Inner For Loops - Patterns Alphabet Patterns

n = int(input("Enter rows: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
