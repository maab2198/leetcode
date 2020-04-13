class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or not k or k == len(nums):
            return
        k = k % len(nums)
        nums[:k],nums[k:] = nums[-k:],nums[:-k]
        return 
