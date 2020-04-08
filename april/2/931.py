from functools import lru_cache
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])
        for i in range(n-2,-1,-1):
            for j in range(m):
                A[i][j] += min(A[i+1][max(0,j-1):min(j+2,m)])
        return min(A[0])


#### recursion version
from functools import lru_cache
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])
        @lru_cache(None)
        def dp(i, j):
            if i == n:
                return 0
            if j < 0 or j > m-1:
                return float('inf')
            return A[i][j] + min(dp(i+1,j),dp(i+1,j-1),dp(i+1,j+1))

        for j in range(0,m):
            A[0][j] = dp(0,j)
        return min(A[0])

