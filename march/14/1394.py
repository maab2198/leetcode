class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = 0
        prev = -1
        arr.sort()
        arr.append(-1)
        n = -1
        for i in range(0,len(arr)):
            count +=1
            if prev != arr[i]:
                if prev == count:
                    n = max(n,count)
                count = 0
            prev = arr[i]
        return n
            
        