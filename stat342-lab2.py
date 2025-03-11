import math
import random 
import numpy as np 



# Example of a 2D array using nested lists
# Creating a 3x4 array (3 rows, 4 columns)
array = [
    [0, 0.5, 0.5, 0, 0],  # State 1 -> 0 
    [0, 0, 0.5, 0.5, 0],  # State 3 -> 1 
    [0.5, 0, 0, 0.5, 0], # State 4 -> 2 (fixed typo in 0,5 -> 0.5)
    [0.5, 0, 0, 0, 0.5], # State 7 -> 3 
    [0, 0, 0, 0, 1]  # State 9 -> 4 
]
q_array = [[0, 0.5, 0.5, 0], 
           [0, 0, 0.5, 0.5], 
           [0.5, 0, 0, 0.5], 
           [0.5, 0, 0, 0]]





def calculate_expected_time_to_win(prob_array):
    array = np.array(prob_array)
    
    n_matrix = np.linalg.inv(np.eye(array.shape[0]) - array)
    
    t_matrix = n_matrix @ np.ones((array.shape[0], 1))
    return t_matrix[0]


def calculate_expected_state7_visits(prob_array): 
    # The expected number of visits to state 7 is given that we started in state 1 is given by 
    # the 0, 3 entry of the matrix N=(I-Q)^-1
    array = np.array(prob_array)
    n_matrix = np.linalg.inv(np.eye(array.shape[0]) - array)
    return n_matrix[0, 3]

    
def run_game(): 
    
    player_position = 0 # Initially in Box 1 
    rounds = 0 
    num_times_in_state7 = 0
    while player_position != 4: 
        player_position = run_round(player_position)
        rounds += 1 
        if player_position == 3: 
            num_times_in_state7 += 1 

    return rounds, num_times_in_state7

def print_state(player_position): 
    if player_position == 0: 
        print("Player is in Box 1")
    elif player_position == 1: 
        print("Player is in Box 3")
    elif player_position == 2: 
        print("Player is in Box 4")
    elif player_position == 3: 
        print("Player is in Box 7")
    elif player_position == 4: 
        print("Player is in Box 9")
        

def run_round(player_position): 
    # Generate a random number
    pos = player_position 
    rand = random.random() 
    
    i = 0 
    while rand >= 0: 
        rand -= array[pos][i]
        i+=1
    i -= 1 
    return i

    



if __name__ == "__main__":

    print(f"The expected number of rounds to win is {round(calculate_expected_time_to_win(q_array)[0], 4)}")
    print(f"The expected number of visits to state 7 is {round(calculate_expected_state7_visits(q_array), 4)}")

    # Run the game 1000 times and print the average number of rounds and the average number of times in state 7
    num_runs = 1000
    total_rounds = 0
    total_times_in_state7 = 0
    for i in range(num_runs):
        rounds, num_times_in_state7 = run_game()
        total_rounds += rounds
        total_times_in_state7 += num_times_in_state7
    print(f"Average number of rounds: {total_rounds / num_runs}")
    print(f"Average number of times in state 7: {total_times_in_state7 / num_runs}")
