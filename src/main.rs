use std::time::Instant;
use std::error::Error;
use my_cereal_lib::{average_sugars_by_calorie_range, get_memory_usage};

fn main() -> Result<(), Box<dyn Error>> {
    let start = Instant::now();
    let initial_memory = get_memory_usage();

    let file_path = "data/cereal.csv";
    let average_sugars = average_sugars_by_calorie_range(file_path)?;

    let final_memory = get_memory_usage();
    let memory_used = final_memory - initial_memory;

    for (range, avg_sugar) in &average_sugars {
        println!("Average sugars for cereals with {}: {:.7}", range, avg_sugar);
    }

    let duration = start.elapsed();
    println!("\nExecution Time: {:?}", duration);
    println!("Memory Used: {} KB", memory_used);

    Ok(())
}
