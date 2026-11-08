animals = [{"Dog":True},
           {"Cat":True},
           {"Cow":False},
           {"Elephant":False}
           ]
for animal in animals:
    for name, is_pet in animal.items():
        if is_pet:
            print(f"A {name} would make a great pet")
print("All these animals have paws (I hope)")