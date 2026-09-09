# Problem 77: Increasing + Decreasing: Using a single recursive function, print numbers in increasing order and then decreasing order. Increasing + Decreasing: Using a single recursive function, print numbers in increasing order and then decreasing order. Nested Loops / Inner For Loops - Patterns Star Patterns 78 Right-angled triangle (stars)  * ** *** **** Nested Loops / Inner For Loops - Patterns Star Patterns 79 Inverted right-angled triangle **** *** ** * Nested Loops / Inner For Loops - Patterns Star Patterns 80 Right-aligned triangle    * ** *** **** Nested Loops / Inner For Loops - Patterns Star Patterns 81 Inverted right-aligned triangle **** *** ** * Nested Loops / Inner For Loops - Patterns Star Patterns 82 Pyramid (centered)    * *** ***** ******* Nested Loops / Inner For Loops - Patterns Star Patterns 83 Inverted pyramid ******* ***** *** * Nested Loops / Inner For Loops - Patterns Star Patterns 84 Diamond shape    * *** ***** ******* ***** *** * Nested Loops / Inner For Loops - Patterns Star Patterns 85 Hollow rectangle * * * * * *       * *       * * * * * * Nested Loops / Inner For Loops - Patterns Star Patterns 86 Hollow right-angled triangle * ** * * **** Nested Loops / Inner For Loops - Patterns Star Patterns 87 Sandglass / Hourglass ******* ***** *** * *** ***** ******* Nested Loops / Inner For Loops - Patterns Number Patterns

def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n)
    print_numbers(n - 1)

n = int(input("Enter N: "))
print_numbers(n)
