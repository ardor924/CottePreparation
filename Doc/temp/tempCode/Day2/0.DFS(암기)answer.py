graph = {
            0 : [1,3,6],
            1 : [0,3],
            2 : [3],
            3 : [0,1,2,7],
            4 : [5],
            5 : [4,6,7],
            6 : [0,5],
            7 : [3,5],
         }


def dfs(cur_v) : 
    visited[cur_v] = True
    for next_v in graph[cur_v] :
        if next_v not in visited :
            dfs(next_v)
            
visited ={}


print(dfs(0))