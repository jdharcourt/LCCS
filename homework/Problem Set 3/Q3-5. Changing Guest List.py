# James Harcourt
# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.


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