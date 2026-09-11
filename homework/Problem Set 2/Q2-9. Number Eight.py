# James Harcourt
# Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results. You should create four lines that look like this:
import math
from random import randint

previous = []

# Why not
for i in range(10000): #Iterate 1000 times

    a = randint(1, 10000) # Generate randinits a + b
    b = randint(1, 1000)
    # Cycle through math operators until an answer of 8 is reached, then print the equation 
    
    plus = a + b
    minus = a - b
    multiply = a * b
    divide = a / b

    
    if plus == 8 and plus not in previous:
        message = f"{a} + {b} is equal to 8"
        print(message)
        previous.append(message)

    if minus == 8 and minus not in previous:
        message = f"{a} - {b} is equal to 8"
        print(message)
        previous.append(message)

    if multiply == 8 and multiply not in previous:
        message = f"{a} x {b} is equal to 8"
        print(message)
        previous.append(message)

    if divide == 8 and divide not in previous:
        message = f"{a} / {b} is equal to 8"
        print(message)
        previous.append(message)