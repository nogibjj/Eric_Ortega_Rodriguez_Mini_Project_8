import pandas as pd

def average_sugars_by_calorie_range():
# Load the CSV 
    df = pd.read_csv("cereal.csv")
    
    ranges = [(i, i + 50) for i in range(0, 300, 50)]
    ranges.append((300, float('inf')))
    range_labels = [f"{low}-{high} calories" if high != float('inf') else "Over 300 calories" for low, high in ranges]

    # Calculate average sugars for each calorie range
    average_sugars = {}
    for (low, high), label in zip(ranges, range_labels):
        filtered_df = df[(df['calories'] > low) & (df['calories'] <= high)]
        avg_sugar = filtered_df['sugars'].mean()
        
        # Only add to results if avg_sugar is a valid number (excluding nan values)
        if not pd.isna(avg_sugar):
            average_sugars[label] = avg_sugar

    # Print the results without NaN values
    for label, avg_sugar in average_sugars.items():
        print(f"Average sugars for cereals with {label}: {avg_sugar:.2f}")

if __name__ == "__main__":
    average_sugars_by_calorie_range()