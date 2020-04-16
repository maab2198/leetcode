class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        R = 0
        L = 1
        res = []
        for i in range(0,len(nums)):
            R = R // nums[i] if R else reduce(lambda x, y: x * y, nums[i+1:], 1)
            res.append(R*L)
            L = L * nums[i]
        return res
        
