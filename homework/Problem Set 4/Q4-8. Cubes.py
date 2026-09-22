# James Harcourt
# A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10). Use a for loop with the range function, and append each cubed number to the end of your list. Print out the value of each cube.

cubed = []

for i in range(1,11):
    cube = i ** 3
    cubed.append(cube)

for i in cubed:
    print(i)