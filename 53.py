class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(nums)
        if max_sum <= 0:
            return max_sum
        curr_sum, max_sum = 0,0
        for el in nums:
            curr_sum +=el
            if curr_sum < 0:
                curr_sum = 0
            if max_sum < curr_sum:
                max_sum = curr_sum
        return max_sum 
        