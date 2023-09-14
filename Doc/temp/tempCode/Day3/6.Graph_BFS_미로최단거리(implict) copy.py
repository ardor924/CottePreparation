from collections import deque

def shortestPathBinaryMatrix(grid) : 
    shortest = -1
    cnt = 0
    row_len = len(grid)
    col_len = len(grid[0])
    # 2차원  복사 (1row에 있는 모든 col을 -999로 초기화)   
    visited = [[False] * col_len for _ in range(row_len)]
    dr = [1, 1, 0, -1, -1, -1, 0, 1]
    dc = [0, 1, 1, 1, 0 ,-1 ,-1 ,-1]
    
    def bfs(r,c) :
        q = deque()
        q.append([r,c])
        # 방문
        visited[r][c] = True
        while q : 
            current_point = q.popleft()
            r = current_point[0]
            c = current_point[1]   
            # dfs(next_v)
            for i in range(8) :
                next_r = r + dr[i]
                next_c = c + dc[i]
                if (
                    0<= next_r < row_len 
                    and 0<= next_c < col_len
                    and grid[next_r][next_c] == "1"  
                    ) : 
                
        # start_v, cur_distance <= queue.dequeue()
        # if 목적지 도착 :
            # return cur_distance    
        # 8가지 방향의 next_v
            # _next_v, nextdistance(= cur_distance +1) 를 queue.dequeue()
            # visited 체크



grid = [
[0, 0, 0, 1, 0, 0, 0],
[0, 1, 1, 1, 0, 1, 0],
[0, 1, 0, 0, 0, 1, 0],
[0, 0, 0, 1, 1, 1, 0],
[0, 1, 0, 0, 0, 0, 0]
]

