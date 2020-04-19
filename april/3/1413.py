class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        m = min(nums)
        startValue = 1
        if m <=0:
            k = nums
            index = 0
            for i in range(1,len(nums)):
                k[i]= k[i-1] + nums[i]
            s = min(k)
            startValue = 1 - s if s < 0 else 1
        return startValue
           
