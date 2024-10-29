import pandas as pd
import time
import memory_profiler  



def average_sugars_by_calorie_range():
    # Load the CSV
    df = pd.read_csv("data/cereal.csv")

    # Define calorie ranges and labels
    ranges = [
        (0, 50),
        (50, 100),
        (100, 150),
        (150, 200),
        (300, float('inf'))
    ]
    range_labels = [
        "0-50 calories", "50-100 calories", "100-150 calories",
        "150-200 calories", "Over 300 calories"
    ]

    # Calculate average sugars for each calorie range
    average_sugars = {}
    for (low, high), label in zip(ranges, range_labels):
        if high == float('inf'):
            filtered_df = df[df['calories'] > low]
        else:
            filtered_df = df[(df['calories'] > low) & (df['calories'] <= high)]
        
        # Print debug information for filtered_df
        print(f"\nRange: {label}")
        print(filtered_df)

        avg_sugar = filtered_df['sugars'].mean()
        
        # Only add to results if avg_sugar is a valid number (excluding NaN values)
        if not pd.isna(avg_sugar):
            average_sugars[label] = avg_sugar

    return average_sugars

if __name__ == "__main__":
    # Track the time and memory usage
    start_time = time.time()
    mem_usage = memory_usage((average_sugars_by_calorie_range,), interval=0.1, timeout=None)
    end_time = time.time()
    
    # Print the time and memory used
    print(f"\nExecution Time: {end_time - start_time:.2f} seconds")
    print(f"Peak Memory Usage: {max(mem_usage):.2f} MB")
