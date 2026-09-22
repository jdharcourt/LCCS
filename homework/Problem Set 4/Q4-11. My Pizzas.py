# James Harcourt
# Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas.
pizza = ["Hawaian", "Peperoni", "Cheese"]
friends_pizza = pizza[:]
friends_pizza.append("BBQ")

for pizza in pizza:
    print(f"I love {pizza} pizza")
print("I really love pizza!")


for pizza in friends_pizza:
    print(f"My Friend loves {pizza} pizza")
print("He really love pizza!")