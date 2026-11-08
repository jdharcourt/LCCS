# Question 16(a)
# Examination Number:
from random import choice

fruits = ['apple', 'cherry', 'orange']

apples = 0
cherries = 0
oranges = 0


random_fruit_1 = choice(fruits) 
random_fruit_2 = choice(fruits) 
random_fruit_3 = choice(fruits)

print("Random Fruit 1: ", random_fruit_1)
print("Random Fruit 1: ", random_fruit_2)
print("Random Fruit 1: ", random_fruit_3)

print(f"The first fruit is: {random_fruit_1} \n")

if random_fruit_1 == random_fruit_2:
    print("First pair match")

    if random_fruit_1 and random_fruit_1 == "cherry":
        print("First pair are cherries")




if len({random_fruit_1,random_fruit_2,random_fruit_3}) < 3:
    print("Matching Pair")

for i in range(100):
    random_fruit = choice(fruits)

    if random_fruit == "cherry":
        cherries += 1
    elif random_fruit == "apple":
        apples += 1
    else:
        oranges += 1

print(f"Apples: {apples}")
print(f"Oranges: {oranges}")
print(f"Cheeries: {cherries}")