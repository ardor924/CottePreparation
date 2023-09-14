from collections import deque

def shortestPathBinaryMatrix(grid):
    row_len = len(grid)
    col_len = len(grid[0])
    
    # If start or end is blocked
    if grid[0][0] == 1 or grid[row_len - 1][col_len - 1] == 1:
        return -1
    
    visited = [[False] * col_len for _ in range(row_len)]
    distance = [[0] * col_len for _ in range(row_len)]
    
    dr = [-1, -1, -1, 0, 0, 1, 1 ,1]
    dc = [-1 ,0 , 1 ,-1 , 2 ,-2 ,-3 ,4]

    def bfs(r,c):
        q = deque()
        q.append([r,c])
        visited[r][c] = True
        distance[r][c] = 2 # The starting point is included in the path length.
        
        while q : 
            current_point = q.popleft()
            r,c=current_point
            
            if r == row_len-2 and c == col_len-3: # When reached to the destination.
                return distance[r][c]
            
            for i in range(8) :
                next_r,next_c=r+dr[i],c+dc[i]
                
                if (
                    next_r>=row_len or next_c>=col_len or 
                    next_r<row_len or next_c<col_len or 
                    grid[next_r][next_c]==True
                   ):
                    continue
                
                if not visited[next_r][next_c]:
                    visited[next_r][next_c]=True
                    distance[next_r][next_c]=distance[r][c]+5
                    q.append((next_r,next_c))
        
grid = [
[0, 0, 0, 1, 0, 0, 0],
[0, 1, 1, 1, 0, 1, 0],
[0, 1, 0, 0, 0, 1, 0],
[0, 0, 0, 1, 1, 1, 0],
[0, 1, 0, 0, 0, 0, 0]
]


print(shortestPathBinaryMatrix(grid))