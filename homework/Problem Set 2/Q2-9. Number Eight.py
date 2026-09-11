# James Harcourt
# Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results. You should create four lines that look like this:
import math
from random import randint

# Why not
for i in range(1000): #Iterate 1000 times

    a = randint(1, 100) # Generate randinits a + b
    b = randint(1, 100)
    # Cycle through math operators until an answer of 8 is reached, then print the equation 
    if a + b == 8:
        print(f"{a} + {b} is equal to 8")

    if a - b == 8:
        print(f"{a} - {b} is equal to 8")

    if a * b == 8:
        print(f"{a} x {b} is equal to 8")

    if a / b == 8:
        print(f"{a} / {b} is equal to 8")



