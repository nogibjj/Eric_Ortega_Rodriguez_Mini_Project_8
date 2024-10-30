[![CI/CD](https://github.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_8/actions/workflows/rust_CI.yml/badge.svg)](https://github.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_8/actions/workflows/rust_CI.yml) [![Python CI](https://github.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_8/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/Eric_Ortega_Rodriguez_Mini_Project_8/actions/workflows/CI.yml)
# Mini Project 8: Rewrite a Python Script in Rust


<p align="center">
  <img src="image-1.png" alt="Cereal Data Project" width="400"/>
</p>

<p align="center"><b>Cereal Data Project</b></p>

## Eric Ortega Rodriguez 

## Project Overview

This project involves rewriting a Python script for processing cereal data in Python and Rust. The primary objective is to highlight Rust's performance benefits, focusing on improved speed and memory efficiency. The Python script calculates the average sugar content of cereals across different calorie ranges, and the Rust version retains this functionality while being more optimal as it pertains to its resources.

Additionally, a CI/CD pipeline using GitHub Actions has been set up to automate the build, test, and artifact generation processes for the Rust project.

## Requirements

- **Rewrite a Python Script**: Take a Python script that processes cereal data and converts it to Rust, maintaining the original functionality.
- **Highlight Performance Improvements**: Demonstrate improvements in speed and memory usage with the Rust implementation.
- **CI/CD Pipeline**: Automate the build and test process using GitHub Actions.

## Features

- **Average Sugar Calculation by Calorie Range**: The program processes a cereal dataset, calculating the average sugar content for cereals within specified calorie ranges (e.g., 0-50, 50-100, up to over 300 calories).
- **Performance Optimization**: The Rust implementation provides improved performance and memory usage, especially when processing large datasets.
- **CI/CD Pipeline**: A GitHub Actions workflow has been set up to automatically test, build, and create artifacts for each commit.

## Deliverables 

- **Python and Rust Scripts**: Both the original Python script and the Rust version are included in this repository.
- **Performance Comparison Report**: A report detailing the improvements in speed and memory usage achieved with Rust.

## Using This Repo 

To build and run the project, ensure you have the following installed:

- **Rust**: Install Rust from [rust-lang.org](https://www.rust-lang.org/tools/install).
- **Cargo**: The Rust package manager (`cargo`) is required to build and run the project.
- **Git**: A GitHub account and Git installation to clone the repository.
- **CI/CD**: GitHub Actions setup for continuous integration and deployment.

## Data Used can be found [here](https://www.kaggle.com/datasets/crawford/80-cereals)

- A quick glimpse of the data 

| name                      | mfr   | type   |   calories |   protein |   fat |   sodium |   fiber |   carbo |   sugars |   potass |   vitamins |   shelf |   weight |   cups |   rating |
|:--------------------------|:------|:-------|-----------:|----------:|------:|---------:|--------:|--------:|---------:|---------:|-----------:|--------:|---------:|-------:|---------:|
| 100% Bran                 | N     | C      |         70 |         4 |     1 |      130 |     10 |     5   |        6 |       280 |         25 |       3 |      1   |   0.33 |   68.4   |
| 100% Natural Bran         | Q     | C      |        120 |         3 |     5 |        15 |      2 |     8   |        8 |       135 |          0 |       3 |      1   |   1    |   33.2   |
| All-Bran                  | K     | C      |         70 |         4 |     1 |      260 |      9 |     7   |        5 |       320 |         25 |       3 |      1   |   0.33 |   59.4   |
| All-Bran with Extra Fiber | K     | C      |         50 |         4 |     0 |      140 |     14 |     8   |        0 |       330 |         25 |       3 |      1   |   0.5  |   93.7   |
| Almond Delight            | R     | C      |        110 |         2 |     2 |      200 |      1 |    14   |        8 |        -1 |          25 |       3 |      1   |   0.75 |   34.4   |


## Rust vs. Python 
![alt text](image.png)

|                    | Python                        | Rust                        | Improvement (Rust vs. Python) |
|--------------------|-------------------------------|-----------------------------|-------------------------------|
| **Execution Time** | 0.0043 s                      | 50.8 ms                     | Rust faster by x 84.31        |
| **Memory Usage**   | 140 KB                        | 1.196 MB                    | Rust lower by x 8.54          |

