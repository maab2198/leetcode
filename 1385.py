class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        counter = 0
        for el1 in arr1:
            for el2 in arr2:
                if abs(el1 - el2) <= d:
                    counter +=1
                    break
        return len(arr1) - counter

        