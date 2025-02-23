import math
import random 
import matplotlib.pyplot as plt 

def run_simulation(num_games):

    playerAwins = 0 
    playerBwins = 0 
    for i in range(num_games):
        if play_game(initial_amount=10, total_dollars=20, p=0.49): 
            playerAwins += 1 
        else: 
            playerBwins += 1 

    print(f"Player A wins {playerAwins} times")
    print(f"Player B wins {playerBwins} times")

    print(f"Probability that player A wins: {playerAwins/num_games}")


def play_game(initial_amount, total_dollars, p): 
    n = total_dollars
    i = initial_amount
    rounds = 0
    
    while(i > 0 and i < n):
        rounds += 1 
        if play_round(p): 
            i += 1 
        else: 
            i -= 1 
        
    
    return i == n, rounds  # true if player A wins, false if player B wins 


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




def q4a_plot():
    n=20
    i=n/2 
    p=0.5 
    rounds = 0
    
    i_values = [i]
    round_numbers = [0]
    
    while(i > 0 and i < n):
        rounds += 1 
        if play_round(p): 
            i += 1 
        else: 
            i -= 1 
            i_values.append(i)
            round_numbers.append(rounds)
    
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


def q4b_plot():
    n=20 
    p=0.44
    startingAmounts = [i for i in range(21)]
    average_game_length = []    
    for j in startingAmounts: 
        total_length = 0 
        num_games = 1000
        for i in range(num_games): 
            _, rounds = play_game(j,n, p)
            total_length += rounds 
        average_game_length.append(total_length/num_games)

    plt.figure(figsize=(10, 6))
    plt.plot(startingAmounts, average_game_length, '-b', label='Average game length')
    plt.xlabel('Starting Amount for A ($)')
    plt.ylabel('Average Game Length')
    plt.title('Average Game Length (over 1000 trials) vs. Starting Amount')
    plt.legend()
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    q4a_plot()
    q4b_plot()







