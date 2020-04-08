# class Solution:
#     def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
#         counter = 0
#         for el1 in arr1:
#             for el2 in arr2:
#                 if abs(el1 - el2) <= d:
#                     counter +=1
#                     break
#         return len(arr1) - counter

# faster with n logn idea
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = len(arr1)
        n = len(arr2)
        for el in arr1:
            mid = bisect.bisect(arr2,el)
            if (0<=mid<n and abs(arr2[mid]-el)<=d) or (0<=mid-1<n and abs(arr2[mid-1]-el)<=d):
                count-=1
        return count