import random
import time

wins = 0
ties = 0
lost = 0


try:
    number = int(input("How many games?: "))
except:
    print("Please only enter a number. \n") 

moves = {
    'rock' : 'scissors',
    'paper' : 'rock',
    'scissors': 'paper'
}


start = time.time()
choices = list(moves.keys())
def turn():
    win = False
    tie = False

    chosen = random.choice(choices)
    chosen2 = random.choice(choices)
    '''
    while True:
        user = str(input('Enter rock, scissors, or paper: ')).lower()
        if user in moves:
            break
        else:
            print("Please only enter rock, paper or scissors\n")
    '''


    if chosen2 == chosen:
        tie = True
    elif moves[chosen2] == chosen:
        win = True
    else:
        win = False

    return win, tie


for i in range(number):
    win, tie = turn()
    if win:
        wins += 1
    elif tie:
        ties += 1
    else:
        lost += 1

end = time.time()
total_t = end - start

print()
print(f"Completed in {total_t}")

print(
    "\n-------Stats------- \n"
    f"Wins: {wins}\n"
    f"Losses: {lost}\n"
    f"Ties: {ties}\n"
    "------------------- \n"
)