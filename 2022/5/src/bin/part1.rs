use std::fs;

use aoc_day_5::process_part_1;

fn main() {
    let input = fs::read_to_string("input.txt").expect("Unable to read file");
    let result = process_part_1(input);
    println!("{}", result);
}
