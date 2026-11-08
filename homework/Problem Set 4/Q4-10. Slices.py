# James Harcourt
# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

multiples = []

for i in range(1,31):
    if i % 3 == 0:
        s = str(i)
        multiples.append(s)

for i in multiples:
    print(i)

print(multiples[-3:])

print(multiples[:3])
print(multiples[:2])