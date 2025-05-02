import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Read the CSV file
    data = pd.read_csv('retinalgf.csv')
    
    # Create histogram
    plt.figure(figsize=(10, 6))
    plt.hist(data['ISI'], bins=30, edgecolor='black')
    plt.title('Histogram of Inter-Spike Intervals (ISI)')
    plt.xlabel('ISI Values')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # Save the plot
    plt.savefig('isi_histogram.png')
    plt.close()

if __name__ == "__main__":
    main()
