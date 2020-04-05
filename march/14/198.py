class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        if len(nums) ==1:
            return nums[0]
        prev = nums[0] 
        curr = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            prev,curr = curr, max(prev+nums[i],curr)
        return curr