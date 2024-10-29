use csv::ReaderBuilder;
use ndarray::Array1;
use ndarray_stats::QuantileExt;
use serde::Deserialize;
use std::error::Error;
use std::f64;

#[derive(Debug, Deserialize)]
struct Cereal {
    calories: Option<f64>,
    sugars: Option<f64>,
}

fn average_sugars_by_calorie_range(file_path: &str) -> Result<(), Box<dyn Error>> {
    let mut reader = ReaderBuilder::new().from_path(file_path)?;
    let mut cereals = Vec::new();

    // Read and parse each row into a Cereal struct
    for result in reader.deserialize() {
        let record: Cereal = result?;
        cereals.push(record);
    }

    // Define calorie ranges and labels
    let ranges = vec![(0.0, 50.0), (50.0, 100.0), (100.0, 150.0), (150.0, 200.0), (200.0, 250.0), (250.0, 300.0), (300.0, f64::INFINITY)];
    let labels = vec!["0-50 calories", "50-100 calories", "100-150 calories", "150-200 calories", "200-250 calories", "250-300 calories", "Over 300 calories"];

    // Calculate average sugars for each of our calorie ranges 
    for (i, (low, high)) in ranges.iter().enumerate() {
        let filtered_sugars: Vec<f64> = cereals
            .iter()
            .filter(|c| match c.calories {
                Some(cal) if cal > *low && cal <= *high => c.sugars.is_some(),
                _ => false,
            })
            .map(|c| c.sugars.unwrap())
            .collect();

        // Calculating average sugar for the filtered cereals
        if !filtered_sugars.is_empty() {
            let sugar_array = Array1::from(filtered_sugars);
            let avg_sugar = sugar_array.mean().unwrap_or(0.0);
            println!("Average sugars for cereals with {}: {:.2}", labels[i], avg_sugar);
        }
    }

    Ok(())
}

fn main() {
    if let Err(e) = average_sugars_by_calorie_range("cereal.csv") {
        eprintln!("Error: {}", e);
    }
}
