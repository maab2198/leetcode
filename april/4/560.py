class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = {}
        if n ==1:
            return 1 if nums[0] ==  k else 0
        s,count =  0,0
        for i in range(n):
            d[s] = d.get(s,0) +1
            s +=nums[i]
            if (s - k) in d:
                count += d[s - k]
        return count
