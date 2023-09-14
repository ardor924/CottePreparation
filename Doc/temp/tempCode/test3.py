class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]

        RIGHT, LEFT, UP, DOWN = (0, 1), (0, -1), (-1, 0), (1, 0)
        UPRIGHT, UPLEFT, DOWNRIGHT, DOWNLEFT = (-1, 1), (-1,-1), (1 , 1) , (1 ,- 1)

        directions = [RIGHT , LEFT , UP , DOWN , UPRIGHT , UPLEFT ,DOWNRIGHT ,DOWNLEFT]

        def bfs(r, c):
            if grid[r][c] == 1:
                return -1

            q = deque()
            q.append((r, c, 1))
            visited[r][c] = True

            while q:
                cur_r, cur_c, cur_dist = q.popleft()
                if cur_r == row_len - 1 and cur_c == col_len - 1:
                    return cur_dist

                for dir in directions:
                    next_r = cur_r + dir[0]
                    next_c = cur_c + dir[1]
                    if (
                        0 <= next_r < row_len
                        and 0 <= next_c < col_len
                        and grid[next_r][next_c] == 0
                    ):
                        if visited[next_r][next_c] == False:
                            q.append((next_r, next_c, cur_dist + 1))
                            visited[next_r][next_c] = True

            return -1

        return bfs(0, 0)