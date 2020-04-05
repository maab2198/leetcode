class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:        
        # f[i] = cost[i] +  min(f[i+1],f[i+2])
        n = len(cost)
        f = cost.copy()
        for i in range(n-3, -1,-1):
            f[i] +=min(f[i+1],f[i+2])
        return min(f[0],f[1])
    
        # fastest
        # dp1,dp2 = cost[0],cost[1]
        # for i in range(2,len(cost)):
        #     dp1,dp2 = dp2,min(dp2,dp1)+cost[i]
        # return min(dp2,dp1)