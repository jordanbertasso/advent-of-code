use std::io::{self, Read};

fn main() {
    let mut buffer = Vec::new();
    let mut stdin = io::stdin();
    stdin.read_to_end(&mut buffer).unwrap();

    // Convert the buffer to a string
    let contents = String::from_utf8(buffer).unwrap();

    // Split contents by newline
    let lines = contents.split('\n');

    let mut prev = -1;
    let mut count = 0;

    for line in lines {
        if prev == -1 {
            prev = line.parse::<i32>().expect("Could not parse line");
            continue;
        }

        let current = match line.parse::<i32>() {
            Ok(n) => n,
            Err(_) => break,
        };

        if current > prev {
            count += 1;
        }

        prev = current;
    }

    println!("Count: {}", count);
}
