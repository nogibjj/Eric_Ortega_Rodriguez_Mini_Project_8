import pandas as pd
import time
import psutil

# Direct URL to the CSV file on GitHub
file_url = "https://github.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_8/raw/refs/heads/main/data/cereal.csv"

try:
    # Load CSV data directly from the URL
    df = pd.read_csv(file_url)
except Exception as e:
    raise FileNotFoundError(f"Failed to load the file from {file_url}: {e}")

required_columns = {"calories", "sugars"}
if not required_columns.issubset(df.columns):
    raise ValueError(f"The CSV file must contain the following columns: {', '.join(required_columns)}")

def average_sugars_by_calorie_range(data_frame: pd.DataFrame):
    ranges = [
        (0.0, 50.0),
        (50.0, 100.0),
        (100.0, 150.0),
        (150.0, 200.0),
        (300.0, float("inf")),
    ]
    range_labels = [
        "0-50 calories",
        "50-100 calories",
        "100-150 calories",
        "150-200 calories",
        "Over 300 calories",
    ]

    range_sugar_totals = [0.0] * len(range_labels)
    range_counts = [0] * len(range_labels)

    for _, row in data_frame.iterrows():
        calories, sugars = row["calories"], row["sugars"]
        for i, (low, high) in enumerate(ranges):
            if low <= calories < high:
                range_sugar_totals[i] += sugars
                range_counts[i] += 1
                break

    average_sugars = {label: (range_sugar_totals[i] / range_counts[i] if range_counts[i] > 0 else 0.0)
                      for i, label in enumerate(range_labels)}

    return average_sugars

def main():
    start_time = time.time()
    process = psutil.Process()
    initial_memory = process.memory_info().rss / 1024 / 1024

    average_sugars = average_sugars_by_calorie_range(df)

    final_memory = process.memory_info().rss / 1024 / 1024
    memory_used = final_memory - initial_memory

    for range_label, avg_sugar in average_sugars.items():
        print(f"Average sugars for cereals with {range_label}: {avg_sugar:.2f}")

    end_time = time.time()
    print(f"\nExecution Time: {end_time - start_time:.4f} seconds")
    print(f"Memory Used: {memory_used:.2f} MB")

if __name__ == "__main__":
    main()
