class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = len(nums)-1
        j = 1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= k:
                k = i
        return k == 0
        
