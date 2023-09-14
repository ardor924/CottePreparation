def isValid(r,c) :
    return 0


def dfs(r,c) :
    visited[r][c] = True 
    for i in range(4) :
        next_r = r + dr[i]
        next_c = c + dc[i]
        if isValid(next_r,next_c) :
            if not visited[next_r][next_c] :
                dfs(next_r,next_c)
                    
                    
                    
grid = []
row_len , col_len = len(grid) , len(grid[0])
visited = [[False] * col_len for _ in range(row_len)] 
dr = [0,1,0,-1]        
dc = [1,0,-1,0]

dfs(0,0)        
        
        