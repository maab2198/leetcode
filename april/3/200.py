class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n ==0:
            return 0
        m = len(grid[0])
        def dfs(i,j,visited):
            visited[i][j] = True
            if grid[i][j] == "0":
                return
            # print((i,j), end = ' ')             
            if j +1 < m and not visited[i][j+1]:
                dfs(i,j+1,visited)
            if i+1 < n and not visited[i+1][j]:
                dfs(i+1,j,visited)
            if i-1 >= 0 and not visited[i-1][j]:
                dfs(i-1,j,visited)
            if j-1 >= 0 and not visited[i][j-1]:
                dfs(i,j-1,visited)
            return 
        visited = [[False for el in range(m)] for k in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] =="1":
                    count+=1
                    dfs(i,j,visited)
        return count
