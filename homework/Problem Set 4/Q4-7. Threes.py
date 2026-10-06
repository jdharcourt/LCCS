# James Harcourt
# Make a list of the multiples of 3, from 3 to 30, using the range() function. Use a for loop to print the numbers in your list.

multiples = []

for i in range(1,31):
    if i % 3 == 0:
        s = str(i)
        multiples.append(s)

for i in multiples:
    print(i)