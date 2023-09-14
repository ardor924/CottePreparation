#==================================================================
#               [그래프] Number of islands
#==================================================================

'''Instruction
'1'(육지)과 '0'(물)으로 구성된 지도를 나타내는 m x n 2D 이진 격자 격자가 주어질 때, 섬의 개수를 반환합니다.

섬은 물로 둘러싸여 있으며 인접한 땅을 가로 또는 세로로 연결하여 형성됩니다. 그리드의 네 모서리가 모두 물로 둘러싸여 있다고 가정할 수 있습니다.


예시 1:

입력: 그리드 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
출력: 1
예 2:

입력: 그리드 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
출력: 3
'''
# URL : https://leetcode.com/problems/number-of-islands/


# 학습용 def코드 
#------------------------   
def numIslands(grid) :
    if not grid or not grid[0]:
        return 0
    row_len = len(grid)
    col_len = len(grid[0])
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    def is_valid(r,c):
        return 0 <= r < row_len and 0 <= c < col_len and grid[r][c] == '1'
    def dfs(r,c):
        if not is_valid(r,c): 
            return
        
        grid[r][c] = '2'
        
        for dr, dc in directions:
            dfs(r + dr,c + dc)
    island_count = 0
    for r in range(row_len):
        for c in range(col_len):
            if is_valid(r,c):
                dfs(r,c)
                island_count += 1
            
    return island_count

#==================================================================

grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]

result = numIslands(grid)
print(f'정답 : {result}')