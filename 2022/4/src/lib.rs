pub struct Range {
    start: u32,
    end: u32,
}

impl Range {
    fn contains(&self, other: &Range) -> bool {
        other.start >= self.start && other.end <= self.end
    }

    fn overlaps(&self, other: &Range) -> bool {
        (other.start >= self.start && other.start <= self.end)
            || (self.start >= other.start && self.start <= other.end)
    }
}

pub fn process_part_1(input: String) -> u32 {
    let mut count = 0;

    input.lines().for_each(|l| {
        let l = l.trim();
        let split: Vec<&str> = l.split(',').collect();
        let (one, two) = (split[0], split[1]);

        let one_split: Vec<&str> = one.split('-').collect();
        let two_split: Vec<&str> = two.split('-').collect();

        let one_range = Range {
            start: one_split[0].parse().unwrap(),
            end: one_split[1].parse().unwrap(),
        };
        let two_range = Range {
            start: two_split[0].parse().unwrap(),
            end: two_split[1].parse().unwrap(),
        };

        if one_range.contains(&two_range) || two_range.contains(&one_range) {
            count += 1;
        }
    });

    count
}

pub fn process_part_2(input: String) -> u32 {
    let mut count = 0;

    input.lines().for_each(|l| {
        let l = l.trim();
        let split: Vec<&str> = l.split(',').collect();
        let (one, two) = (split[0], split[1]);

        let one_split: Vec<&str> = one.split('-').collect();
        let two_split: Vec<&str> = two.split('-').collect();

        let one_range = Range {
            start: one_split[0].parse().unwrap(),
            end: one_split[1].parse().unwrap(),
        };
        let two_range = Range {
            start: two_split[0].parse().unwrap(),
            end: two_split[1].parse().unwrap(),
        };

        if one_range.overlaps(&two_range) {
            count += 1;
        }
    });

    count
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = process_part_1(
            "2-4,6-8
            2-3,4-5
            5-7,7-9
            2-8,3-7
            6-6,4-6
            2-6,4-8"
                .to_owned(),
        );
        assert_eq!(result, 2);
    }

    #[test]
    fn part2() {
        let result = process_part_2(
            "2-4,6-8
            2-3,4-5
            5-7,7-9
            2-8,3-7
            6-6,4-6
            2-6,4-8"
                .to_owned(),
        );
        assert_eq!(result, 4);
    }
}
