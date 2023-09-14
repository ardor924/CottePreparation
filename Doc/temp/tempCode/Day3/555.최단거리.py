from collections import deque

def shortestPathBinaryMatrix(grid):
    row_len = len(grid)
    col_len = len(grid[0])
    visited = [[False] * col_len for _ in range(row_len)]  