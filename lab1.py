import math
import random 

random.seed(42)  # You can use any integer value as the seed

def run_simulation(num_games):

    playerAwins = 0 
    playerBwins = 0 
    for i in range(num_games):
        if play_game(): 
            playerAwins += 1 
        else: 
            playerBwins += 1 

    print(f"Player A wins {playerAwins} times")
    print(f"Player B wins {playerBwins} times")

    print(f"Probability that player A wins: {playerAwins/num_games}")


def play_game(): 
    n = 200 
    i = n/2
    p = 0.49 
    while(i > 0 and i < n):
        if play_round(p): 
            i += 1 
        else: 
            i -= 1 

    return i == n # true if player A wins, false if player B wins 


def play_round(prob): # i is the amount of money player 1 has, j is the amount of money player 2 has

# return true if player 1 wins, 
# return false if player 2 wins 
    # generate a random number between 0 and 1 
    r = random.random()

    if r <= prob:
        return True
    else:
        return False
    





if __name__ == "__main__":

    run_simulation(1000)





