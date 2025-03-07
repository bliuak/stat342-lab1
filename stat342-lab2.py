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
def run_game(): 
    
    player_position = 0 # Initially in Box 1 
    rounds = 0 
    print_state(player_position)  # Print initial state
    while player_position != 4: 
        player_position = run_round(player_position)
        rounds += 1 

    print(f"Player wins in {rounds} rounds")


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
    print_state(i)
    return i

    



if __name__ == "__main__":

    print(calculate_expected_time_to_win(q_array))
    run_game() 

