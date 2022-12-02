use std::io::{self, Read};

#[derive(Eq, PartialEq)]
struct Move {
    // Points for playing the drawing move
    draw: u32,
    // Points for playing the winning move
    win: u32,
    // Points for playing the losing move
    lose: u32,
}

const ROCK: Move = Move {
    // Rock
    draw: 1,
    // Paper
    win: 2,
    // Scissors
    lose: 3,
};
const PAPER: Move = Move {
    // Paper
    draw: 2,
    // Scissors
    win: 3,
    // Rock
    lose: 1,
};
const SCISSORS: Move = Move {
    // Scissors
    draw: 3,
    // Rock
    win: 1,
    // Paper
    lose: 2,
};

fn main() {
    let round1 = false;
    let mut buffer = Vec::new();
    let mut stdin = io::stdin();
    stdin.read_to_end(&mut buffer).unwrap();

    // Convert the buffer to a string
    let contents = String::from_utf8(buffer).unwrap();

    // Split contents by newline
    let rounds = contents.split('\n');

    let mut score = 0;

    // Iterate over the lines
    for round in rounds {
        let (them, second_letter) = round.split_at(round.find(' ').unwrap());

        let them = match them.trim() {
            "A" => ROCK,
            "B" => PAPER,
            "C" => SCISSORS,
            _ => panic!("No matching move found"),
        };

        if round1 {
            score += match second_letter.trim() {
                // Rock
                "X" => {
                    1 + match them {
                        ROCK => 3,
                        PAPER => 0,
                        SCISSORS => 6,
                        _ => panic!("Not a valid move"),
                    }
                }
                // Paper
                "Y" => {
                    2 + match them {
                        ROCK => 6,
                        PAPER => 3,
                        SCISSORS => 0,
                        _ => panic!("Not a valid move"),
                    }
                }
                // Scissors
                "Z" => {
                    3 + match them {
                        ROCK => 0,
                        PAPER => 6,
                        SCISSORS => 3,
                        _ => panic!("Not a valid move"),
                    }
                }
                _ => panic!("Not a valid outcome"),
            };
        } else {
            score += match second_letter.trim() {
                // Win
                "Z" => 6 + them.win,
                // Lose
                "X" => them.lose,
                // Draw
                "Y" => 3 + them.draw,
                _ => panic!("Not a valid outcome"),
            };
        }
    }
    println!("{}", score);
}
