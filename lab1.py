import math
import random 
import matplotlib.pyplot as plt 

#random.seed(42) 

def run_simulation(num_games):

    playerAwins = 0 
    playerBwins = 0 
    for i in range(num_games):
        if play_game(plot=True): 
            playerAwins += 1 
        else: 
            playerBwins += 1 

    print(f"Player A wins {playerAwins} times")
    print(f"Player B wins {playerBwins} times")

    print(f"Probability that player A wins: {playerAwins/num_games}")


def play_game(plot=False): 
    n = 20 
    i = n/2
    p = 0.49 
    rounds = 0
    
    # Keep track of i values and rounds if plotting
    if plot:
        i_values = [i]
        round_numbers = [0]
    
    while(i > 0 and i < n):
        rounds += 1 
        if play_round(p): 
            i += 1 
        else: 
            i -= 1 
        
        if plot:
            i_values.append(i)
            round_numbers.append(rounds)
    
    if plot:
        plt.figure(figsize=(10, 6))
        plt.plot(round_numbers, i_values, '-b', label='Player A money')
        plt.axhline(y=n, color='g', linestyle='--', label='Win threshold')
        plt.axhline(y=0, color='r', linestyle='--', label='Loss threshold')
        plt.xlabel('Round')
        plt.ylabel('Amount for A ($)')
        plt.title('Amount for A vs. Round')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    return i == n  # true if player A wins, false if player B wins 


def play_round(prob): # i is the amount of money player 1 has, j is the amount of money player 2 has

# return true if player 1 wins, 
# return false if player 2 wins 
    # generate a random number between 0 and 1 
    r = random.random()

    if r <= prob:
        return True
    else:
        return False
    


def run_simulation_q3(num_games): 
    playerAwins = 0 
    playerBwins = 0 
    for i in range(num_games): 
        if play_game_q3(): 
            playerAwins += 1 
        else: 
            playerBwins += 1 

    print(f"Player A wins {playerAwins} times")
    print(f"Player B wins {playerBwins} times")
    print(f"Probability that player A wins: {playerAwins/num_games}")

def play_game_q3(): 
    n = 200
    i = n/2 
    p = 0.49 
    while(i > 0 and i < n): 
        won = play_round_q3(p)
        if won == 0: 
            i += 1 
        elif won == 1: 
            i -= 1 
        else: 
            continue 
    return i == n # if player A wins = true, if player B wins = false        
def play_round_q3(p): 

    r = random.random()
    if r <= p: 
        return 0  # Player A wins 
    elif r > p and r <= 2*p: 
        return 1  # Player B wins 
    elif r > 2*p: 
        return 2  # Tie 




if __name__ == "__main__":

    run_simulation(1000)





