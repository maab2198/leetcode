class NumArray:
    def __init__(self, nums: List[int]):
        if len(nums)< 1:
            return
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        self.s = nums

    def sumRange(self, i: int, j: int) -> int:
            return self.s[j] if i ==0 else self.s[j] - self.s[i-1]

##faster
# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.sum = [0] * len(nums)
#         add = 0
#         for i in range (len(nums)):
#             add += nums[i]
#             self.sum[i] = add

#     def sumRange(self, i: int, j: int) -> int:
#         if i == 0:
#             return self.sum[j]
#         else:
#             return self.sum[j] - self.sum[i - 1]