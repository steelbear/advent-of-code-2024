#[cfg(feature = "day04")]
pub mod day04 {
    use std::path::Path;
    use std::fs::read_to_string;

    type Delta = (bool, usize, bool, usize);

    fn is_valid(
        x: usize, y: usize, 
        delta: Delta,
        w: usize, h: usize
    ) -> bool {
        let (pos_x, dx, pos_y, dy) = delta;

        if (!pos_x && (x < dx)) || (!pos_y && (y < dy)) {
            return false;
        }

        let (new_x, new_y) = move_point(x, y, delta);

        new_x < w && new_y < h
    }

    fn move_point(
        x: usize, y: usize,
        delta: Delta
    ) -> (usize, usize) {
        let (pos_x, dx, pos_y, dy) = delta;

        let new_x = if pos_x { x + dx } else { x - dx };
        let new_y = if pos_y { y + dy } else { y - dy };

        (new_x, new_y)
    }

    fn find_all(
        mat: &Vec<Vec<u8>>, pattern: &Vec<u8>,
        mut start_x: usize, mut start_y: usize,
        dr: Delta, dc: Delta
    ) -> u32 {
        let w = mat[0].len();
        let h = mat.len();

        let mut count = 0;
        let mut i_pat;
        let mut x;
        let mut y;
        loop {
            x = start_x;
            y = start_y;

            i_pat = 0;
            loop {
                if mat[y][x] == pattern[i_pat] {
                    i_pat += 1;
                } else if mat[y][x] == pattern[0] {
                    i_pat = 1;
                } else {
                    i_pat = 0;
                }
                if i_pat == pattern.len() {
                    i_pat = 0;
                    count += 1;
                }

                if is_valid(x, y, dr, w, h) {
                    (x, y) = move_point(x, y, dr);
                } else {
                    break;
                }
            }

            if is_valid(start_x, start_y, dc, w, h) {
                (start_x, start_y) = move_point(start_x, start_y, dc);
            } else {
                break;
            }
        }
        count
    }

    pub fn part01(path: &Path) -> u32 {
        let mut mat: Vec<Vec<u8>> = Vec::new();

        for line in read_to_string(path).unwrap().lines() {
            mat.push(line.trim().into());
        };

        let w = mat[0].len();
        let h = mat.len();
        let search_strategies: [(usize, usize, Delta, Delta); 12] = [
            (0, 0, (true, 1, true, 0), (true, 0, true, 1)), // left -> right
            (w - 1, 0, (false, 1, true, 0), (true, 0, true, 1)), // right -> left
            (0, 0, (true, 0, true, 1), (true, 1, true, 0)), // top -> bottom
            (0, h - 1, (true, 0, false, 1), (true, 1, true, 0)), // bottom -> top
            (w - 1, 0, (true, 1, true, 1), (false, 1, true, 0)), // top left -> bottom right
            (0, 1, (true, 1, true, 1), (true, 0, true, 1)),
            (w - 1, 0, (false, 1, false, 1), (true, 0, true, 1)), // bottom right -> top left
            (w - 2, h - 1, (false, 1, false, 1), (false, 1, true, 0)),
            (0, 0, (true, 1, false, 1), (true, 0, true, 1)), // bottom left -> top right
            (1, h - 1, (true, 1, false, 1), (true, 1, true, 0)),
            (0, 0, (false, 1, true, 1), (true, 1, true, 0)), // top right -> bottom left
            (w - 1, 1, (false, 1, true, 1), (true, 0, true, 1)),
        ];

        let pattern: Vec<u8> = "XMAS".into();
        let mut count = 0;

        for (x, y, dr, dc) in search_strategies {
            count += find_all(&mat, &pattern, x, y, dr, dc);
        }

        count
    }

    fn is_matched(mat: &Vec<Vec<u8>>, x: usize, y: usize) -> bool {
        mat[y + 1][x + 1] == b'A' && (
            (mat[y + 0][x + 0] == b'M' && mat[y + 2][x + 2] == b'S') ||
            (mat[y + 0][x + 0] == b'S' && mat[y + 2][x + 2] == b'M')
        ) && (
            (mat[y + 0][x + 2] == b'M' && mat[y + 2][x + 0] == b'S') ||
            (mat[y + 0][x + 2] == b'S' && mat[y + 2][x + 0] == b'M')
        )
    }

    pub fn part02(path: &Path) -> u32 {
        let mut mat: Vec<Vec<u8>> = Vec::new();

        for line in read_to_string(path).unwrap().lines() {
            mat.push(line.trim().into());
        };

        let mut count = 0;
        for y in 0..(mat.len() - 2) {
            for x in 0..(mat[0].len() - 2) {
                if is_matched(&mat, x, y) {
                    count += 1;
                }
            }
        }

        count
    }
}

#[cfg(test)]
#[cfg(feature = "day04")]
mod tests {
    use std::path::Path;
    use super::day04;

    #[test]
    fn test_day04_part01_example() {
        let input_file = Path::new("../inputs/day04_example.txt");
        let result = day04::part01(input_file);
        println!("day04 part01 example => {}", result);
    }

    #[test]
    fn test_day04_part01() {
        let input_file = Path::new("../inputs/day04.txt");
        let result = day04::part01(input_file);
        println!("day04 part01 => {}", result);
    }

    #[test]
    fn test_day04_part02_example() {
        let input_file = Path::new("../inputs/day04_example.txt");
        let result = day04::part02(input_file);
        println!("day04 part02 example => {}", result);
    }

    #[test]
    fn test_day04_part02() {
        let input_file = Path::new("../inputs/day04.txt");
        let result = day04::part02(input_file);
        println!("day04 part02 => {}", result);
    }
}