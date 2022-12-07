use regex::Regex;
use std::vec;

pub fn process_part_1(input: String) -> String {
    // TODO: Parse the stacks later
    // Check every n*4 + 1th character to get the letter at that height for a stack
    // Add each letter to a vec as I encounter them
    // Reverse each vec to have the top crate at the end of the vec

    // let mut stacks: Vec<Vec<char>> = vec![
    //     vec!['W', 'D', 'G', 'B', 'H', 'R', 'V'],
    //     vec!['J', 'N', 'G', 'C', 'R', 'F'],
    //     vec!['L', 'S', 'F', 'H', 'D', 'N', 'J'],
    //     vec!['J', 'D', 'S', 'V'],
    //     vec!['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V'],
    //     vec!['P', 'G', 'H', 'C', 'M'],
    //     vec!['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
    //     vec!['S', 'J', 'R'],
    //     vec!['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M'],
    // ];
    let mut stacks: Vec<Vec<char>> = vec![vec!['Z', 'N'], vec!['M', 'C', 'D'], vec!['P']];

    input
        .lines()
        .skip_while(|l| !l.trim().starts_with('m'))
        .for_each(|l| {
            // println!("{}", l);
            let l = l.trim();
            let re = Regex::new(r"^move (\d+) from (\d+) to (\d+)$").unwrap();

            let caps = match re.captures(l) {
                Some(x) => x,
                None => return,
            };

            let amount: usize = caps.get(1).unwrap().as_str().parse().unwrap();
            let from_stack: usize = caps.get(2).unwrap().as_str().parse().unwrap();
            let to_stack: usize = caps.get(3).unwrap().as_str().parse().unwrap();

            let from_stack = &mut stacks[from_stack - 1];

            let move_stack: Vec<char> = from_stack
                .iter()
                .rev()
                .take(amount)
                .map(|c| c.to_owned())
                .collect();

            for _ in 0..amount as u32 {
                from_stack.pop();
            }

            // dbg!(amount, from_stack, to_stack);

            let to_stack = &mut stacks[to_stack - 1];

            for x in move_stack {
                to_stack.push(x);
            }
        });

    let starts = stacks
        .iter()
        .map(|stack| *stack.iter().rev().peekable().peek().unwrap());
    String::from_iter(starts)
}

pub fn process_part_2(input: String) -> String {
    // TODO: Parse the stacks later
    // Check every n*4 + 1th character to get the letter at that height for a stack
    // Add each letter to a vec as I encounter them
    // Reverse each vec to have the top crate at the end of the vec

    let mut stacks: Vec<Vec<char>> = vec![
        vec!['W', 'D', 'G', 'B', 'H', 'R', 'V'],
        vec!['J', 'N', 'G', 'C', 'R', 'F'],
        vec!['L', 'S', 'F', 'H', 'D', 'N', 'J'],
        vec!['J', 'D', 'S', 'V'],
        vec!['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V'],
        vec!['P', 'G', 'H', 'C', 'M'],
        vec!['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
        vec!['S', 'J', 'R'],
        vec!['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M'],
    ];
    // let mut stacks: Vec<Vec<char>> = vec![vec!['Z', 'N'], vec!['M', 'C', 'D'], vec!['P']];

    input
        .lines()
        .skip_while(|l| !l.trim().starts_with('m'))
        .for_each(|l| {
            // println!("{}", l);
            let l = l.trim();
            let re = Regex::new(r"^move (\d+) from (\d+) to (\d+)$").unwrap();

            let caps = match re.captures(l) {
                Some(x) => x,
                None => return,
            };

            let amount: usize = caps.get(1).unwrap().as_str().parse().unwrap();
            let from_stack: usize = caps.get(2).unwrap().as_str().parse().unwrap();
            let to_stack: usize = caps.get(3).unwrap().as_str().parse().unwrap();

            let from_stack = &mut stacks[from_stack - 1];

            let move_stack: Vec<char> = from_stack[from_stack.len() - amount..]
                .iter()
                .map(|c| c.to_owned())
                .collect();

            for _ in 0..amount as u32 {
                from_stack.pop();
            }

            // dbg!(amount, from_stack, to_stack);

            let to_stack = &mut stacks[to_stack - 1];

            for x in move_stack {
                to_stack.push(x);
            }
        });

    let starts = stacks
        .iter()
        .map(|stack| *stack.iter().rev().peekable().peek().unwrap());
    String::from_iter(starts)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = process_part_1(
            "
                [D]    
            [N] [C]    
            [Z] [M] [P]
             1   2   3 
            
            move 1 from 2 to 1
            move 3 from 1 to 3
            move 2 from 2 to 1
            move 1 from 1 to 2
            "
            .to_owned(),
        );
        assert_eq!(result, "CMZ");
    }

    #[test]
    fn part2() {
        let result = process_part_2(
            "
                [D]    
            [N] [C]    
            [Z] [M] [P]
             1   2   3 
            
            move 1 from 2 to 1
            move 3 from 1 to 3
            move 2 from 2 to 1
            move 1 from 1 to 2
            "
            .to_owned(),
        );
        assert_eq!(result, "MCD");
    }
}
