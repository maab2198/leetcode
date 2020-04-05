class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        res = []
        max_s = sum(nums)
        s = 0
        for el in nums:
            s += el
            max_s -= el
            res.append(el)
            if s > max_s:
                break
        return res
        
        