# James Harcourt
# Q5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#
# Make a list of five or more usernames called current_users.
# Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
# Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users = ["James", 'Daithi', "Alex", 'Brian']

new_users = ["Matthew", "James", "Hugo", 'Brian']

con = False

for i, user in enumerate(new_users):
    con = False

    while con == False:
        if any(user.lower() == x.lower() for x in current_users):
            new = str(input(f"This username is taken. Enter a new username for {user}: ")).strip()
            if any(new.lower() == x.lower() for x in current_users):
                continue
            else:
                new_users[i] = new
                con = True
        else:
            con = True

for user in new_users:
    current_users.append(user.title())

for user in current_users:
    print(user)
        

