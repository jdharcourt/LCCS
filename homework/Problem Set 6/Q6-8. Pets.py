# James Harcourt
# Q6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

pets = [
    {"name":'Teddy',"Animal":"dog", "owner":'James'},
    {"name":'Lilly',"Animal":"Cat", "owner":'Mark'},
    {"name":'Freddy',"Animal":"Fish", "owner":'Luke'}
]

for pet in pets:
    print(f"Name: {pet['name'].title()}")
    print(f"Animal: {pet['Animal'].title()}")
    print(f"Owner: {pet['owner'].title()}\n")