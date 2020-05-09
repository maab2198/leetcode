class Solution:
    # 56 ms
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) ==2:
            return true
        dif_y = coordinates[0][1] - coordinates[1][1]

        dif_x = coordinates[0][0] - coordinates[1][0]
        
        k = dif_y/dif_x if dif_x else 0
        for i in range(2,len(coordinates)):
            dif_y,dif_x = coordinates[i-1][1] - coordinates[i][1],coordinates[i-1][0] - coordinates[i][0]
            check = dif_y/dif_x if dif_x else 0
            if check != k:
                return False
        return True
    # 60 ms
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