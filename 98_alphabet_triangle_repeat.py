# Problem 98: Alphabet triangle (row repeat) A B B C C C D D D D Nested Loops / Inner For Loops - Patterns Alphabet Patterns

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    print(chr(64 + i) * i)
