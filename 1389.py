# my second version 
# time 28ms
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        arr= []
        for i in range(len(nums)):
            arr.insert(index[i],nums[i])
        return arr
            


# fastest result with 16 ms time
# class Solution:
#     def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
#         result = []
#         for n,i in zip(nums,index):
#             if(i>=len(result)):
#                 result.append(n)
#             else:
#                 result = result[:i] + [n] + result[i:]
#         return result    