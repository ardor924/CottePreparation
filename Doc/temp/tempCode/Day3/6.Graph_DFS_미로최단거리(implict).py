def shortestPathBinaryMatrix(grid) : 
    shortest = -1
    cnt = 0
    row_len = len(grid)
    col_len = len(grid[0])
    # 2차원  복사 (1row에 있는 모든 col을 False로 초기화)   
    visited = [[False] * col_len for _ in range(row_len)]
    dr = [1, 1, 0, -1, -1, -1, 0, 1]
    dc = [0, 1, 1, 1, 0 ,-1 ,-1 ,-1]

    def dfs(r,c) :
        # 방문
        visited[r][c] = True
        # dfs(next_v)
        for i in range(8) :
            next_r = r + dr[i]
            next_c = r + dc[i]






grid = [
[0, 0, 0, 1, 0, 0, 0],
[0, 1, 1, 1, 0, 1, 0],
[0, 1, 0, 0, 0, 1, 0],
[0, 0, 0, 1, 1, 1, 0],
[0, 1, 0, 0, 0, 0, 0]
]

# row_len = len(grid)
# col_len = len(grid[0])
# visited = [[False] * col_len for _ in range(row_len)]
# print(visited)
