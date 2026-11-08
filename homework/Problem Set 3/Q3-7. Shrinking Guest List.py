# James Harcourt
# You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.

names = ["Steve Jobs", "Bill Gates", "Sam Altman", "Lenardo Da Vinci"]


for name in names:
    print(f"I would like to ivite you to dinner {name}")


unavailable = input("Who cant make it? ")

for name in names:
    if unavailable == name or unavailable.upper() == name or unavailable.lower() == name or unavailable.title() == name:
        names.remove(name)

new = input("Who else do you want to invite? ")
new = new.title()

names.append(new)

for name in names:
    print(f"I would like to ivite you to dinner {name}")


print("I have just found a bigger table")
print("I am now inviting\n")

new_names = ["Steve Wozniac", "Tim Berner-lee", "Marie Currie"]

names = names + new_names

for name in names:
    print(f"I would like to ivite you to dinner, {name}")

print("Sorry for the confusion, only 2 can come now :( ")

while len(names) > 2:
    name = names.pop()
    print(f"Sorry, {name}, you can no longer come :( ")

