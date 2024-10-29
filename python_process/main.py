import pandas as pd
import time
import psutil  # pylint: disable=import-error
import os

# Load the CSV file with the absolute path
file_path = "/Users/ericortega/Eric_Ortega_Rodriguez_Mini_Project_8/data/cereal.csv"
df = pd.read_csv(file_path)  # Load the CSV once at the start

def average_sugars_by_calorie_range(df: pd.DataFrame):
    # Define calorie ranges and corresponding labels
    ranges = [
        (0.0, 50.0),
        (50.0, 100.0),
        (100.0, 150.0),
        (150.0, 200.0),
        (300.0, float('inf'))
    ]
    range_labels = [
        "0-50 calories", "50-100 calories", "100-150 calories",
        "150-200 calories", "Over 300 calories"
    ]

    # Prepare lists to accumulate sugar totals and counts for each range
    range_sugar_totals = [0.0] * len(range_labels)
    range_counts = [0] * len(range_labels)

    # Process each record in the DataFrame
    for _, row in df.iterrows():
        calories, sugars = row['calories'], row['sugars']
        for i, (low, high) in enumerate(ranges):
            if low < calories <= high:
                range_sugar_totals[i] += sugars
                range_counts[i] += 1
                break

    # Calculate the average sugars for each calorie range
    average_sugars = {}
    for i, label in enumerate(range_labels):
        if range_counts[i] > 0:
            average_sugars[label] = range_sugar_totals[i] / range_counts[i]

    return average_sugars

def main():
    # Start measuring time and initial memory usage
    start_time = time.time()
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024  # Memory in KB
    
    # Calculate average sugars by calorie range
    average_sugars = average_sugars_by_calorie_range(df)

    # Measure memory usage after execution
    final_memory = process.memory_info().rss / 1024  # Memory in KB
    memory_used = final_memory - initial_memory

    # Display the results
    for range_label, avg_sugar in average_sugars.items():
        print(f"Average sugars for cereals with {range_label}: {avg_sugar:.2f}")

    # Print execution time and memory usage
    end_time = time.time()
    print(f"\nExecution Time: {end_time - start_time:.4f} seconds")
    print(f"Memory Used: {memory_used:.2f} KB")

if __name__ == "__main__":
    main()
