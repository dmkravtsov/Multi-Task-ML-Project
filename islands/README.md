# Island Counting Problem

## Problem Description

You are given a matrix **M x N** where each cell is either **1** (representing land) or **0** (representing ocean). The task is to count how many distinct islands are present in the matrix. An island is formed by connecting adjacent land cells horizontally, vertically, or diagonally.

## Solution Approach

To solve this problem, we use a **Depth-First Search (DFS)** approach:

1. **DFS** is initiated at each unvisited land cell (1).
2. All connected land cells are marked as visited (set to 0) to ensure we don’t count the same island multiple times.
3. Each time we find an unvisited land cell, we increment the island count.

## How the Code Works

1. The function `count_islands(matrix)` iterates over every cell in the matrix.
2. When a land cell (1) is found, it triggers the `explore_island(row, col)` function that uses DFS to mark all the connected cells of that island.
3. We continue this process until all cells have been checked, and the final count of islands is returned.

## How to Use the Script

1. Save the Python script as `count_islands.py`.
2. Run the script from the terminal with the following command:


python count_islands.py
