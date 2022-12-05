use std::collections::HashSet;

pub fn process_part_1(input: String) -> u32 {
    let mut common_chars = vec![];

    input.lines().for_each(|mut line| {
        line = line.trim();
        let first_half = &line[..line.len() / 2];
        let second_half = &line[line.len() / 2..];

        let compartment_1: HashSet<char> = HashSet::from_iter(first_half.chars());
        let compartment_2: HashSet<char> = HashSet::from_iter(second_half.chars());

        let common: Vec<&char> = compartment_1.intersection(&compartment_2).take(1).collect();

        common_chars.push(common[0].to_owned());
    });

    common_chars
        .iter()
        .map(|c| {
            if c.is_lowercase() {
                *c as u32 - 'a' as u32 + 1
            } else {
                *c as u32 - 'A' as u32 + 27
            }
        })
        .sum()
}

pub fn process_part_2(input: String) -> u32 {
    let mut common_chars = vec![];

    let lines: Vec<&str> = input.lines().map(|l| l.trim()).collect();

    lines.chunks(3).for_each(|chunk| {
        let mut lines = chunk.iter();
        let line1 = lines.next().unwrap();
        let line2 = lines.next().unwrap();
        let line3 = lines.next().unwrap();

        let chars1: HashSet<char> = HashSet::from_iter(line1.chars());
        let chars2: HashSet<char> = HashSet::from_iter(line2.chars());
        let chars3: HashSet<char> = HashSet::from_iter(line3.chars());

        let common1: Vec<&char> = chars1.intersection(&chars2).collect();

        for c in common1 {
            if chars3.contains(c) {
                common_chars.push(c.to_owned());
            }
        }
    });

    common_chars
        .iter()
        .map(|c| {
            if c.is_lowercase() {
                *c as u32 - 'a' as u32 + 1
            } else {
                *c as u32 - 'A' as u32 + 27
            }
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = process_part_1(
            "vJrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw"
                .to_owned(),
        );
        assert_eq!(result, 157);
    }

    #[test]
    fn part2() {
        let result = process_part_2(
            "vJrwpWtwJgWrhcsFMMfFFhFp
            jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
            PmmdzqPrVvPwwTWBwg
            wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
            ttgJtRGJQctTZtZT
            CrZsJsPPZsGzwwsLwLmpwMDw"
                .to_owned(),
        );
        assert_eq!(result, 70);
    }
}
