def uniquePaths(m,n) :
    memo = [[False] * n for _ in range(m)]
    def dfs(r,c) :
        if m == 0 and n == 0 :
            memo[r][c] = 1
            return memo[r][c]

        if memo[r][c] == False :
            if r-1 >= 0 :
                unique_paths += dfs(r-1,c)
            if c-1 >= 0 :
                unique_paths += dfs(r,c-1)

            memo[r][c] = unique_paths
        return memo[r][c]
    return dfs(m-1,n-1)
uniquePaths(3,7)
