pub mod day01 {
    use std::collections::HashMap;
    use std::fs::File;
    use std::io::read_to_string;
    use std::iter::zip;
    use std::path::Path;

    pub fn part1(path: &Path) -> u64 {
        let mut left_group: Vec<u64> = Vec::new();
        let mut right_group: Vec<u64> = Vec::new();

        let file = match File::open(path) {
            Err(err) => panic!("Error while reading file: {}", err),
            Ok(file) => file,
        };

        for line in read_to_string(file).unwrap().lines() {
            let numbers: Vec<u64> = match line.split("   ").map(|x| x.parse()).collect() {
                Ok(v) => v,
                Err(err) => panic!("Error while reading file: {}", err),
            };

            if numbers.len() != 2 {
                panic!("Error while parsing inputs: {}", line)
            }

            left_group.push(numbers[0]);
            right_group.push(numbers[1]);
        }

        left_group.sort();
        right_group.sort();

        zip(left_group, right_group)
            .map(|(left, right)| if left > right { left - right } else { right - left })
            .sum()
    }

    pub fn part2(path: &Path) -> u64 {
        let mut similarity: u64 = 0;
        let mut left_counter: HashMap<u64, u64> = HashMap::new();
        let mut right_counter: HashMap<u64, u64> = HashMap::new();

        let file = match File::open(path) {
            Err(err) => panic!("Error while reading file: {}", err),
            Ok(file) => file,
        };

        for line in read_to_string(file).unwrap().lines() {
            let numbers: Vec<u64> = match line.split("   ").map(|x| x.parse()).collect() {
                Ok(v) => v,
                Err(err) => panic!("Error while reading file: {}", err),
            };

            if numbers.len() != 2 {
                panic!("Error while parsing inputs: {}", line)
            }

            left_counter.entry(numbers[0])
                .and_modify(|count| *count += 1)
                .or_insert(1);
            right_counter.entry(numbers[1])
                .and_modify(|count| *count += 1)
                .or_insert(1);
        }

        for id in left_counter.keys() {
            let left_count = left_counter.get(id).unwrap();
            let right_count= right_counter.get(id).or(Some(&0)).unwrap();

            similarity += id * left_count * right_count;
        }

        similarity
    }
}

#[cfg(test)]
pub mod tests {
    use std::path::Path;
    use super::day01;

    #[test]
    pub fn test_day01_part01_example() {
        let input_file = Path::new("../inputs/day01_example.txt");
        let result = day01::part1(&input_file);
        println!("day01 part01 example => {}", result);
    }

    #[test]
    pub fn test_day01_part02_example() {
        let input_file = Path::new("../inputs/day01_example.txt");
        let result = day01::part2(&input_file);
        println!("day01 part02 example => {}", result);
    }

    #[test]
    pub fn test_day01_part01() {
        let input_file = Path::new("../inputs/day01.txt");
        let result = day01::part1(&input_file);
        println!("day01 part01 => {}", result);
    }

    #[test]
    pub fn test_day01_part02() {
        let input_file = Path::new("../inputs/day01.txt");
        let result = day01::part2(&input_file);
        println!("day01 part02 => {}", result);
    }
}