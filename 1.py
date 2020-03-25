class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for i in range(len(nums)):
            j = target - nums[i]
            if j in hash_map:
                    return [hash_map[j], i]
            hash_map[nums[i]] = i 
                     
        