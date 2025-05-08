import matplotlib.pyplot as plt
import numpy as np

def main(): 

   # random_walk_q1(10)
    #random_walk_q1(100)
    #random_walk_q1(1000)
    #random_walk_q1(10000)

    # Run Q2: 100 simulations with n=1000
    #random_walk_q2(100)

    #random_walk_q3(1000)

    random_walk_q4(1000, 0.5, 1.5)


def random_walk_q1(n): 

    stepsize = 1/np.sqrt(n)
    x= np.zeros(n)
    y= np.zeros(n)

    for i in range(n):
        x[i] = i
        if i == 0:
            y[i] = 0
        else: 
            y[i] += np.random.choice([-1,1])*stepsize + y[i-1]

    # Plot the complete path outside the loop
    plt.plot(x, y, 'b-') # Plot x vs y as a continuous blue line
    plt.title(f"1D Random Walk ({n} steps)") # Add a title
    plt.xlabel("Step Number (Time)") # Label x-axis
    plt.ylabel("Position (Y)") # Label y-axis
    plt.grid(True) # Add a grid
    plt.show()

def random_walk_q2(num_simulations):
    n = 1000  # Fixed number of steps
    stepsize = 1 / np.sqrt(n)

    plt.figure(figsize=(12, 8))  # Create a figure to hold all plots

    for _ in range(num_simulations):
        # Initialize position arrays for this simulation
        x = np.zeros(n)
        y = np.zeros(n)

        # Perform the random walk calculation
        for i in range(n):
            x[i] = i
            if i > 0:
                # Calculate next step based on previous position
                y[i] = y[i-1] + np.random.choice([-1, 1]) * stepsize
            # y[0] remains 0 (initial position)

        # Plot this specific walk on the figure
        # Matplotlib cycles colors automatically
        plt.plot(x, y, alpha=0.5) # Use alpha for better visibility with many lines

    # Configure and display the final plot after all simulations are plotted
    plt.title(f"{num_simulations} Random Walks (n={n} steps)")
    plt.xlabel("Step Number (Time)")
    plt.ylabel("Position (Y)")
    plt.grid(True)
    plt.show()

def random_walk_q3(num_simulations):

    n = 1000  # Fixed number of steps
    stepsize = 1 / np.sqrt(n)

    # Array to store the y-position of each simulation at each step
    all_y_positions = np.zeros((num_simulations, n))

    # x values (time steps) are the same for all simulations
    x_steps = np.arange(n)

    for sim_index in range(num_simulations):
        # Initialize y position array for this simulation
        y = np.zeros(n)

        # Perform the random walk calculation
        for i in range(1, n): # Start from step 1
            # Calculate next step based on previous position
            y[i] = y[i-1] + np.random.choice([-1, 1]) * stepsize
        
        # Store the y-path of this simulation
        all_y_positions[sim_index, :] = y

    # Calculate the variance across simulations for each time step
    empirical_variances = np.var(all_y_positions, axis=0)
    
    # Calculate theoretical variance: i * stepsize^2
    theoretical_variances = x_steps * (stepsize**2)

    # Plot the empirical and theoretical variance over time
    plt.figure(figsize=(12, 8))
    plt.plot(x_steps, empirical_variances, label='Empirical Variance')
    plt.plot(x_steps, theoretical_variances, label='Theoretical Variance (t/n)', linestyle='--')
    
    plt.title(f"Variance of Random Walk Position over Time (n={n}, {num_simulations} simulations)")
    plt.xlabel("Step Number (Time, t)")
    plt.ylabel("Variance of Y Position")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # --- Covariance Calculation ---
    idx1, idx2 = 300, 600
    if n > idx1 and n > idx2:
        # Extract positions at the specified steps
        y_at_idx1 = all_y_positions[:, idx1]
        y_at_idx2 = all_y_positions[:, idx2]

        # -- Method 1: Using np.cov (Population Covariance, ddof=0) --
        cov_matrix = np.cov(y_at_idx1, y_at_idx2, ddof=0)
        empirical_covariance_np = cov_matrix[0, 1] # or cov_matrix[1, 0]


        print(f"Empirical Covariance (s=0.3, t=0.6): {empirical_covariance_np:.6f}")
    
    # We now plot the distribution of B(1). 
    plt.figure(figsize=(12, 8))
    plt.hist(all_y_positions[:, -1], bins=30, density=True, alpha=0.7, label='B(1)')
    plt.title('Distribution of B(1)')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

def random_walk_q4(num_simulations, variance1, variance2=None): 
    x = np.zeros(num_simulations)
    y1 = np.zeros(num_simulations)
    y2 = np.zeros(num_simulations)

    # Generate first random walk
    for i in range(num_simulations):
        x[i] = i
        if i == 0:
            y1[i] = 0
        else: 
            y1[i] = y1[i-1] + np.random.normal(0, np.sqrt(variance1/num_simulations))

    # If second variance is provided, generate second random walk
    # If not, only plot the first random walk
    if variance2 is not None:
        for i in range(num_simulations):
            if i == 0:
                y2[i] = 0
            else: 
                y2[i] = y2[i-1] + np.random.normal(0, np.sqrt(variance2/num_simulations))

    # Plot both paths on the same graph
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, 'b-', label=f'σ² = {variance1}')
    if variance2 is not None:
        plt.plot(x, y2, 'r-', label=f'σ² = {variance2}')
    
    plt.title(f"Comparison of Random Walks with Different Variances (n={num_simulations} steps)")
    plt.xlabel("Step Number (Time)")
    plt.ylabel("Position (Y)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    np.random.seed(123)
    main()
