def solution(grid) :
    cnt = 0
    row_len = len(grid)
    col_len = len(grid[0])
    
    visited = [[False] * col_len for _ in range(row_len)]
    dr = [1,0,-1,0]
    dc = [0,1,0,-1]
    
    def dfs(r,c,grid,visited) :
        # 방문
        visited[r][c] = True
        # dfs(next_v)
        for i in range(4) :
            next_r = r + dr[i]
            next_c = c + dc[i]
            if (
                0<= next_r < row_len 
                and 0<= next_c < col_len
                and grid[next_r][next_c] == "1"  
                ) :
                if visited[next_r][next_c] == False :
                    dfs(next_r,next_c,grid,visited)
    
    for r in range(row_len) :
        for c in range(col_len) :
            if grid[r][c] == "1" and visited[r][c] == False :
                dfs(r,c,grid,visited)
                cnt += 1
    
 
 
    
solution(
    grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
)