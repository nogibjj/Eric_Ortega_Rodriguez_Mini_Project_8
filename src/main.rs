use my_project::average_sugars_by_calorie_range;

fn main() {
    // Specify the path to the CSV file in the "data" folder
    let file_path = "data/cereal.cvs";
    
    // Call the function and handle the result
    match average_sugars_by_calorie_range(file_path) {
        Ok(averages) => {
            for (label, avg_sugar) in averages {
                println!("Average sugars for cereals with {}: {:.2}", label, avg_sugar);
            }
        }
        Err(e) => eprintln!("Error calculating averages: {}", e),
    }
}
