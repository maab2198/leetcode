class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if 1 not in nums or 0 not in nums:
            return 0

        mp = {0: -1} 
        prefix_sum = 0
        result = 0
        for idx, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1
            if prefix_sum in mp:
                result = max(result, idx - mp[prefix_sum])
            else:
                mp[prefix_sum] = idx

        return result
        
