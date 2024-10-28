use std::time::Instant;
use std::error::Error;

mod lib;

fn main() -> Result<(), Box<dyn Error>> {
    let start = Instant::now();
    
    // Path to your CSV file
    let file_path = "data/cereal.csv";
    let average_sugars = lib::average_sugars_by_calorie_range(file_path)?;

    // Display the results
    for (range, avg_sugar) in average_sugars {
        println!("Average sugars for cereals with {}: {:.2}", range, avg_sugar);
    }

    // Measure and print elapsed time
    let duration = start.elapsed();
    println!("\nExecution Time: {:?}", duration);

    Ok(())
}
