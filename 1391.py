class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.rules =  {
        1:{"l","r"},
        2:{"t","b"},
        3:{"l","b"},
        4:{"r","b"},
        5:{"l","t"},
        6:{"r","t"}}
        n = len(grid)
        m = len(grid[0])
        r = self.rec(grid,n-1,m-1,{},0)
        return r
    
    def rec(self,grid,i,j,path, prev):
        if i == 0 and j ==0:
            return True
        elif i >= len(grid) or j >=len(grid[0]) or j < 0 or i < 0:
            return False
        
        el = grid[i][j]
        if prev not in self.rules[el] and prev != 0:
            return False


        path[str(i)+" "+str(j)]=0
        ans = set()

        
        if "l" in self.rules[el]:
            if (str(i)+" "+str(j-1)) not in path:
                if self.rec(grid,i,j-1,path,"r"):
                    return True
        if "r" in self.rules[el]:
            if (str(i)+" "+str(j+1)) not in path:
                if self.rec(grid,i,j+1,path,"l"):
                    return True
        if "t" in self.rules[el]:
            if (str(i-1)+" "+str(j)) not in path:
                if self.rec(grid,i-1,j,path,"b"):
                    return True
        if "b" in self.rules[el]:
            if (str(i+1)+" "+str(j)) not in path:
                if self.rec(grid,i+1,j,path,"t"):
                    return True
        return False 
            

            
            
            
        