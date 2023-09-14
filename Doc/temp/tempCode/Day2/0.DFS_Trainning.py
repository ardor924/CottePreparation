# def dfs(graph, start_v):
#     visited = {start_v : True}
#     for next_v in graph[start_v] :
#         if next_v not in visited :
#             dfs(next_v)

#     return list(visited)


# visited = []        
# def dfs(graph, start_v):
#     if start_v not in visited:
#         visited.append(start_v)
#     for next_v in sorted(graph[start_v]):
#         if next_v not in visited:
#             dfs(graph, next_v)
#     result = list(visited)  
#     print(result)     
    # return list(visited)

# visited = []
# def dfs(graph, start_v):
#     if start_v not in visited:
#         visited.append(start_v)
#     for next_v in sorted(graph[start_v]):
#         if next_v not in visited:
#             dfs(graph, next_v)
#     result = list(visited)
#     print(result)


# visited = []        
# def dfs(graph, start_v):
#     if start_v not in visited:
#         visited.append(start_v)
#     for next_v in sorted(graph[start_v]):
#         if next_v not in visited:
#             dfs(graph, next_v)
#     print(visited)
#     return list(visited)  



visited = {}        

def dfs(graph, start_v, depth=0):
    if start_v not in visited:
        visited[start_v] = True
    for next_v in sorted(graph[start_v]):
        if next_v not in visited:
            dfs(graph, next_v, depth+1)
    if depth == 0:  
        print(list(visited.keys()))  




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

dfs(graph, start_v=0)

# print(dfs(graph, start_v=0))



'''



'''