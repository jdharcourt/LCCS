# James Harcourt
# Q5-5. Alien Colours #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#
# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.
# Write three versions of this program, making sure each message is printed for the appropriate colour alien.

color = "red"
points = 0

if color == "green":
    points += 5

elif color == "yellow":
    points += 10
else:
    points += 15


print(f"You earned {points}")