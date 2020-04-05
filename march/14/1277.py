class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix[0])
        n = len(matrix)
        a = matrix
        k = [sum(a[0])]
        for i in range(1,n):
            for j in range(1,m):
                if a[i][j] ==1:
                    a[i][j] = min(a[i][j-1],a[i-1][j-1],a[i-1][j]) +1
            k.append(sum(a[i]))
        return sum(k)        
                        