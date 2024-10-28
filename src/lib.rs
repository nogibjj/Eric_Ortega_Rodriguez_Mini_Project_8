use csv::ReaderBuilder;
use serde::Deserialize;
use std::collections::HashMap;

#[derive(Debug, Deserialize)]
struct Cereal {
    calories: f32,
    sugars: f32,
}

pub fn average_sugars_by_calorie_range(file_path: &str) -> Result<HashMap<String, f32>, Box<dyn std::error::Error>> {
    // Set up the ranges and labels
    let ranges = vec![(0.0, 50.0), (50.0, 100.0), (100.0, 150.0), (150.0, 200.0), (200.0, 250.0), (250.0, 300.0), (300.0, f32::INFINITY)];
    let range_labels: Vec<String> = ranges.iter().map(|&(low, high)| {
        if high == f32::INFINITY {
            "Over 300 calories".to_string()
        } else {
            format!("{}-{} calories", low, high)
        }
    }).collect();

    // Read the CSV file
    let mut rdr = ReaderBuilder::new().from_path(file_path)?;
    let mut data: Vec<Cereal> = Vec::new();
    
    for result in rdr.deserialize() {
        let record: Cereal = result?;
        data.push(record);
    }

    // Calculate average sugars for each calorie range
    let mut average_sugars = HashMap::new();

    for ((low, high), label) in ranges.iter().zip(range_labels.iter()) {
        let filtered: Vec<f32> = data.iter()
            .filter(|cereal| cereal.calories > *low && cereal.calories <= *high)
            .map(|cereal| cereal.sugars)
            .collect();

        if !filtered.is_empty() {
            let avg_sugar: f32 = filtered.iter().sum::<f32>() / filtered.len() as f32;
            average_sugars.insert(label.clone(), avg_sugar);
        }
    }

    // Return the calculated averages as a HashMap
    Ok(average_sugars)
}
