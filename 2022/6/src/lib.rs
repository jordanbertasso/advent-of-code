use std::collections::HashMap;

pub fn process_part_1(input: String) -> u32 {
    let stream = input.trim();

    let mut count = 0;
    let mut seen_chars: HashMap<u32, Vec<char>> = HashMap::new();

    for c in stream.chars() {
        let mut to_remove = vec![];

        for (_, v) in &seen_chars {
            if v.len() == 4 {
                return count;
            }
        }

        for (k, v) in &mut seen_chars {
            if v.contains(&c) {
                to_remove.push(k.to_owned());
            } else {
                v.push(c.to_owned());
            }
        }

        to_remove.iter().for_each(|k| {
            seen_chars.remove(k);
        });
        to_remove.clear();

        seen_chars.insert(count, vec![c]);

        count += 1;
    }

    count
}

pub fn process_part_2(input: String) -> u32 {
    let stream = input.trim();

    let mut count = 0;
    let mut seen_chars: HashMap<u32, Vec<char>> = HashMap::new();

    for c in stream.chars() {
        let mut to_remove = vec![];

        for (_, v) in &seen_chars {
            if v.len() == 14 {
                return count;
            }
        }

        for (k, v) in &mut seen_chars {
            if v.contains(&c) {
                to_remove.push(k.to_owned());
            } else {
                v.push(c.to_owned());
            }
        }

        to_remove.iter().for_each(|k| {
            seen_chars.remove(k);
        });
        to_remove.clear();

        seen_chars.insert(count, vec![c]);

        count += 1;
    }

    count
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = process_part_1("mjqjpqmgbljsphdztnvjfqwrcgsmlb".to_owned());
        assert_eq!(result, 7);
    }

    #[test]
    fn part2() {
        let result = process_part_2("mjqjpqmgbljsphdztnvjfqwrcgsmlb".to_owned());
        assert_eq!(result, 19);
    }
}
