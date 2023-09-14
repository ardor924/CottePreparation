from collections import deque

# def bfs(graph, start_v):
#     q = deque()
#     q.append(start_v)
#     visited = {start_v : True}    
#     while q :
#         curr_v = q.popleft()
#         for next_v in graph[curr_v] :
#             if next_v not in visited :
#                 q.append(next_v)
#                 visited[next_v] = True
                
#     return list(visited)




def bfs(graph, start_v):
    q = deque()
    q.append(start_v)
    visited = {start_v : True}    
    while q :
        curr_v = q.popleft()
        for next_v in graph[curr_v] :
            if next_v not in visited :
                q.append(next_v)
                visited[next_v] = True
                result = list(visited)
    print(result)




graph = {
            0: [1, 3, 6],
            1: [0, 3],
            2: [3],
            3: [0, 1, 2, 7],
            4: [5],
            5: [4, 6, 7],
            6: [0, 5],
            7: [3, 5],
        }

bfs(graph, start_v=0)

# print(bfs(graph, start_v=0))