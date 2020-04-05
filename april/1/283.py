class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = nums.count(0)
        if not count:
            return
        n = len(nums)
        start = nums.index(0)
        if count == n:
            return 
        if start == n - count:
            return
        i = start
        while i < n - count:
            if nums[i] == 0:
                a = nums.pop(i)
                nums.append(a)
                i -=1
            i+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        