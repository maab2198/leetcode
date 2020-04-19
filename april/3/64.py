from functools import lru_cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        dp_table = grid
        
        # Base case:
        # optimization for row_#0
        for x in range(1,m):
            dp_table[0][x] = grid[0][x] + dp_table[0][x-1]

        # optimization for column_#0
        for y in range(1,n):
            dp_table[y][0] = grid[y][0] + dp_table[y-1][0]

        for y in range(1,n):
            for x in range(1,m):
                dp_table[y][x] = grid[y][x] + min( dp_table[y][x-1], dp_table[y-1][x] )       
        return dp_table[n-1][m-1]
