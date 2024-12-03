#[cfg(feature = "day03")]
pub mod day03 {
    use std::path::Path;
    use std::fs::read_to_string;
    use regex::Regex;

    pub fn part01(path: &Path) -> u32 { 
        let mut result = 0;
        let opr_pattern = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
        
        for line in read_to_string(path).unwrap().lines() {
            for (_, [a, b]) in opr_pattern.captures_iter(line).map(|c| c.extract()) {
                let a: u32 = a.parse().unwrap();
                let b: u32 = b.parse().unwrap();
                result += a * b;
            }
        }

        result
    }
    pub fn part02(path: &Path) -> u32 {
        let mut enabled: bool = true;
        let mut result: u32 = 0;
        let opr_pattern = Regex::new(r"mul\((?<a>\d+),(?<b>\d+)\)|(?<do>do)\(\)|(?<dont>don\'t)\(\)").unwrap();

        for line in read_to_string(path).unwrap().lines() {
            for capture in opr_pattern.captures_iter(line) {
                if capture.name("do").is_some() {
                    enabled = true;
                } else if capture.name("dont").is_some() {
                    enabled = false;
                } else if enabled {
                    let a: u32 = capture.name("a").unwrap().as_str().parse().unwrap();
                    let b: u32 = capture.name("b").unwrap().as_str().parse().unwrap();
                    result += a * b;
                }
            }
        }

        result
    }
}

#[cfg(test)]
#[cfg(feature = "day03")]
mod tests {
    use std::path::Path;
    use super::day03;

    #[test]
    fn test_day03_part01_example() {
        let input_file = Path::new("../inputs/day03_example.txt");
        let result = day03::part01(&input_file);
        println!("day03 part01 example => {}", result);
    }

    #[test]
    fn test_day03_part01() {
        let input_file = Path::new("../inputs/day03.txt");
        let result = day03::part01(&input_file);
        println!("day03 part01 example => {}", result);
    }

    #[test]
    fn test_day03_part02_example() {
        let input_file = Path::new("../inputs/day03_example2.txt");
        let result = day03::part02(&input_file);
        println!("day03 part01 example => {}", result);
    }

    #[test]
    fn test_day03_part02() {
        let input_file = Path::new("../inputs/day03.txt");
        let result = day03::part02(&input_file);
        println!("day03 part01 example => {}", result);
    }
}