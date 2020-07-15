class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) ==2:
            return true
        for i in range(2,len(coordinates)):
            a = coordinates[i-2]
            b = coordinates[i-1]
            c = coordinates[i]
            check = a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])
            if check !=0:
                return False
        return True
