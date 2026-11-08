# James Harcourt
# Q6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this section, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.

from random import choice
pizza = {
    'crust': ['thick', "thin"],
    'toppings': ['mushrooms', 'extra cheese', 'pineapple', 'ham', 'pepperoni'],
    }

# Summarize the order.
print(f"You ordered a {choice(pizza['crust'])}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")