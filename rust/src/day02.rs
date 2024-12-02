pub mod day02 {
    use std::fs::File;
    use std::io::read_to_string;
    use std::path::Path;

    pub fn part01(path: &Path) -> i32 {
        let mut total = 0;
        let mut num_unsafe = 0;
        
        let file = match File::open(path) {
            Ok(file) => file,
            Err(err) => panic!("Error while reading file: {}", err),
        };

        for line in read_to_string(file).unwrap().lines() {
            let nums: Vec<i32> = line.split(' ').map(|x| x.parse().unwrap()).collect();
            let diffs: Vec<i32> = (1..nums.len()).map(|i| nums[i] - nums[i - 1]).collect();

            total += 1;
            
            let direction = if diffs[0] > 0 { 1 } else { -1 };
            for diff in diffs {
                let diff = diff * direction;
                if 0 >= diff || diff > 3 {
                    num_unsafe += 1;
                    break;
                }    
            }
        }

        total - num_unsafe
    }

    pub fn part02(path: &Path) -> i32 {
        fn is_safe(nums: &Vec<i32>, ignore: usize) -> bool {
            let mut prev = if ignore == 0 { nums[1] } else { nums[0] };
            let direction = if ignore == 0 {
                if nums[2] - nums[1] > 0 { 1 } else { -1 }
            } else if ignore == 1 {
                if nums[2] - nums[0] >  0 { 1 } else { -1 }
            } else {
                if nums[1] - nums[0] > 0 { 1 } else { -1 }
            };

            for (i, num) in nums.iter().enumerate() {
                if i == 0 || (i == 1 && ignore == 0) || ignore == i {
                    continue;
                }

                let diff = (num - prev) * direction;
                if 0 >= diff || diff > 3 {
                    return false;
                }
                prev = *num;
            }
            return true;
        }

        let mut count = 0;
        let file = match File::open(path) {
            Ok(file) => file,
            Err(err) => panic!("Error while reading file: {}", err),
        };

        for line in read_to_string(file).unwrap().lines() {
            let nums: Vec<i32> = line.split(' ').map(|x| x.parse().unwrap()).collect();
            
            if is_safe(&nums, nums.len()) {
                count += 1;
                continue;
            }

            for i in 0..nums.len() {
                if is_safe(&nums, i) {
                    count += 1;
                    break;
                }
            }
        }

        count
    }
}

#[cfg(test)]
pub mod tests {
    use std::path::Path;
    use super::day02;

    #[test]
    pub fn test_day02_part01_example() {
        let input_file = Path::new("../inputs/day02_example.txt");
        let result = day02::part01(&input_file);
        println!("day02 part01 example => {}", result);
    }

    #[test]
    pub fn test_day02_part01() {
        let input_file = Path::new("../inputs/day02.txt");
        let result = day02::part01(&input_file);
        println!("day02 part01 => {}", result);
    }

    #[test]
    pub fn test_day02_part02_example() {
        let input_file = Path::new("../inputs/day02_example.txt");
        let result = day02::part02(&input_file);
        println!("day02 part02 example => {}", result);
    }

    #[test]
    pub fn test_day02_part02() {
        let input_file = Path::new("../inputs/day02.txt");
        let result = day02::part02(&input_file);
        println!("day02 part02 => {}", result);
    }
}