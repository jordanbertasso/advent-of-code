use std::io::{self, Read};

fn main() {
    let mut buffer = Vec::new();
    let mut stdin = io::stdin();
    stdin.read_to_end(&mut buffer).unwrap();

    // Convert the buffer to a string
    let contents = String::from_utf8(buffer).unwrap();

    // Split contents by newline
    let lines = contents.split('\n');

    let mut sum = 0;
    let mut calories_per_elf = vec![];

    // Iterate over the lines
    for line in lines {
        match line.parse::<i32>() {
            Ok(n) => {
                sum += n;
            }
            Err(_) => {
                calories_per_elf.push(sum);
                sum = 0;
            }
        }
    }
    calories_per_elf.sort();
    calories_per_elf.reverse();

    println!("{}", calories_per_elf[0]);
    // Print the sum of the largest 3 values in the vector
    println!(
        "{}",
        calories_per_elf[0] + calories_per_elf[1] + calories_per_elf[2]
    );
}
