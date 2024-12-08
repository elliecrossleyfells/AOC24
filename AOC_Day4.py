
file_path = "input.txt"

def count_xmas_in_file(file_path):
    # Read the grid from the file
    with open(file_path, "r") as file:
        grid = [line.strip() for line in file.readlines()]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    word = "XMAS"
    word_length = len(word)

    # Define directions as (row_increment, col_increment)
    directions = [
        (0, 1),   # Horizontal (left-to-right)
        (0, -1),  # Horizontal (right-to-left)
        (1, 0),   # Vertical (top-to-bottom)
        (-1, 0),  # Vertical (bottom-to-top)
        (1, 1),   # Diagonal (top-left to bottom-right)
        (-1, -1), # Diagonal (bottom-right to top-left)
        (1, -1),  # Diagonal (top-right to bottom-left)
        (-1, 1),  # Diagonal (bottom-left to top-right)
    ]

    def is_valid(r, c):
        #Check if a position is within the grid.
        return 0 <= r < rows and 0 <= c < cols

    def count_word_from_position(start_r, start_c, direction):
        #Count occurrences of the word starting from a position in a given direction.
        r, c = start_r, start_c
        for i in range(word_length):
            if not is_valid(r, c) or grid[r][c] != word[i]:
                return 0
            r += direction[0]
            c += direction[1]
        return 1  # Found one occurrence

    # Count occurrences of the word in all directions
    total_count = 0
    for r in range(rows):
        for c in range(cols):
            for direction in directions:
                total_count += count_word_from_position(r, c, direction)

    return total_count

def count_x_mas_in_file(file_path):
    # Read the grid from the file
    with open(file_path, "r") as file:
        grid = [line.strip() for line in file.readlines()]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def is_valid(r, c):
        # Check if a position is within the grid
        return 0 <= r < rows and 0 <= c < cols

    def is_x_mas_pattern(center_r, center_c):
        """
        Check if the "X-MAS" pattern exists around the center 'A'.
        The pattern requires:
        - 'A' at the center
        - Diagonal corners containing 'M', 'M', 'S', 'S'
        """
        if not is_valid(center_r, center_c) or grid[center_r][center_c] != 'A':
            return False

        # Define the diagonal corner positions
        corners = [
            (center_r - 1, center_c - 1),  # Upper Left
            (center_r - 1, center_c + 1),  # Upper Right
            (center_r + 1, center_c - 1),  # Lower Left
            (center_r + 1, center_c + 1),  # Lower Right
        ]

        # Validate if all corners are within bounds and have the correct letters
        if all(is_valid(r, c) for r, c in corners):
            corner_values = [grid[r][c] for r, c in corners]
            # Ensure the corners contain 'M', 'M', 'S', 'S' in any order
            if sorted(corner_values) == ['M', 'M', 'S', 'S']:
                # Ensure diagonal pairs are distinct
                ul, ur, dl, dr = corner_values
                return ul != dr and ur != dl

        return False

    # Count all X-MAS patterns
    total_count = 0
    for r in range(1, rows - 1):  # Skip edges (center 'A' needs space)
        for c in range(1, cols - 1):
            if is_x_mas_pattern(r, c):
                total_count += 1

    return total_count


# Main Execution
if __name__ == "__main__":
    # Part 1: Count occurrences of "XMAS"
    part1_count = count_xmas_in_file(file_path)
    print(f"XMAS appears {part1_count} times")

    # Part 2: Count occurrences of "X-MAS" patterns
    part2_count = count_x_mas_in_file(file_path)
    print(f"X-MAS appears {part2_count} times")


