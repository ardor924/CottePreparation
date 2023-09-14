def solution(grid):
    cnt = 0
    row_len = len(grid)
    col_len = len(grid[0])
    visited = [[False] * col_len for _ in range(row_len)]
    for r in range(row_len):
        for c in range(col_len):
            if grid[r][c] == "1" and visited[r][c] == False:
                # dfs(r, c) # 우리의 뇌에 있는 라이브러리에서 가져오면됨
                # bfs(r, c)
                cnt += 1
    return cnt


solution(
    grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
)