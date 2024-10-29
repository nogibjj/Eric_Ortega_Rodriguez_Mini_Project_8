use std::collections::HashMap;
use std::fs::File;
use std::error::Error;
use csv::ReaderBuilder;
use serde::Deserialize;

#[derive(Debug, Deserialize)]
struct CerealRecord {
    calories: f64,
    sugars: f64,
}

#[allow(dead_code)]
pub fn average_sugars_by_calorie_range(file_path: &str) -> Result<HashMap<String, f64>, Box<dyn Error>> {
    let mut reader = ReaderBuilder::new().from_reader(File::open(file_path)?);

    // Define calorie ranges and corresponding labels
    let ranges = [
        (0.0, 50.0),
        (50.0, 100.0),
        (100.0, 150.0),
        (150.0, 200.0),
        (300.0, f64::INFINITY),
    ];
    let range_labels = [
        "0-50 calories",
        "50-100 calories",
        "100-150 calories",
        "150-200 calories",
        "Over 300 calories",
    ];

    // Prepare vectors to accumulate sugar totals and counts for each range
    let mut range_sugar_totals = vec![0.0; range_labels.len()];
    let mut range_counts = vec![0; range_labels.len()];

    // Process each record in the CSV
    for result in reader.deserialize() {
        let record: CerealRecord = result?;
        for (i, &(low, high)) in ranges.iter().enumerate() {
            if record.calories > low && record.calories <= high {
                range_sugar_totals[i] += record.sugars;
                range_counts[i] += 1;
                break;
            }
        }
    }

    // Calculate the average sugars for each calorie range
    let mut average_sugars = HashMap::new();
    for (i, label) in range_labels.iter().enumerate() {
        if range_counts[i] > 0 {
            average_sugars.insert(
                label.to_string(),
                range_sugar_totals[i] / range_counts[i] as f64,
            );
        }
    }
    Ok(average_sugars)
}
