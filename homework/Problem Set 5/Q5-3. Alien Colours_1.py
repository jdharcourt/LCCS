# James Harcourt
# Q5-3. Alien Colours_1: Imagine an alien was just shot down in a game. Create a variable called alien_colour and assign it a value of 'green', 'yellow', or 'red'.
#
# Write an if statement to test whether the alien’s colour is green. If it is, print a message that the player just earned 5 points.
# Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

alien_colour = "green"
points = 0

if alien_colour == "green":
    points += 5

if alien_colour == "red":
    points += 5

print(f"You Earned {points} points")