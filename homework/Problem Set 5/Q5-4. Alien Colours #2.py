# James Harcourt
# Q5-4. Alien Colours #2: Choose a colour for an alien as you did in Exercise 5-3, and write an if-else chain. 
#
# If the alien’s colour is green, print a statement that the player just earned 5 points for shooting the alien.
# If the alien’s colour isn’t green, print a statement that the player just earned 10 points.
# Write one version of this program that runs the if block and another that runs the else block.

color = "red"
points = 0

if color == "green":
    points += 5

else:
    points += 10

print(f"You earned {points}")

