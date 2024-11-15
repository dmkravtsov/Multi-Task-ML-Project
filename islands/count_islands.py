"""
This script counts the number of islands in a matrix.
A matrix cell with 1 represents land, and 0 represents ocean.
"""

def count_islands(matrix):
    # Function to explore and mark all cells of an island
    def explore_island(row, col):
        stack = [(row, col)]  # Stack to keep cells for exploration
        while stack:
            r, c = stack.pop()  # Take the current cell
            if matrix[r][c] == 1:
                matrix[r][c] = 0  # Mark this cell as visited (land becomes ocean)
                # Add neighbors (if they are within the bounds of the map)
                if r > 0: stack.append((r - 1, c))  # up
                if r < len(matrix) - 1: stack.append((r + 1, c))  # down
                if c > 0: stack.append((r, c - 1))  # left
                if c < len(matrix[0]) - 1: stack.append((r, c + 1))  # right

    islands = 0  # Island counter

    # Iterate through each cell in the map
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:  # If land is found
                islands += 1  # New island found
                explore_island(row, col)  # Mark the whole island

    return islands

if __name__ == "__main__":
    # Example matrices for testing
    matrix1 = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 1]
    ]
    matrix2 = [
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0]
    ]
    matrix3 = [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 1]
    ]

    # Test each matrix
    print("Test 1: Number of islands:", count_islands(matrix1))  # Output: 2
    print("Test 2: Number of islands:", count_islands(matrix2))  # Output: 3
    print("Test 3: Number of islands:", count_islands(matrix3))  # Output: 2
