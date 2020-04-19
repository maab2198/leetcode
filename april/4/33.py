class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def search(arr,start, end , target):
            if start > end:
                return -1
            if end == start and target == arr[start]:
                return start
            mid = int((start+end)/2)
            if arr[mid] > target:
                return search(arr,start,mid-1,target)
            if arr[mid] < target:
                return search(arr,mid+1,end,target)
            if arr[mid] == target:
                return mid
            
        def findPivot(arr,low,high):
            if high < low:
                return -1
            if high == low:
                return low
            mid = int((low+high)/2)
            if mid < high and arr[mid]>arr[mid+1]:
                return mid
            if mid > low and arr[mid] < arr[mid-1]:
                return mid -1
            if arr[low]>=arr[mid]:
                return findPivot(arr,low,mid-1)
            return findPivot(arr,mid+1,high)
        
        n = len(nums)
        if n ==0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        if nums[0] < nums[n-1]:
            return search(nums,0,len(nums)-1,target)
        pivot = findPivot(nums,0,n-1)
        if target > nums[pivot]:
            return -1
        arr1 = nums[:pivot+1]
        arr2 = nums[pivot+1:]
        if len(arr2) and target < arr2[-1]:
            res = search(arr2,0,len(arr2)-1,target)
            return (pivot +1 + res) if res >=0 else res
        elif len(arr2) and target ==arr2[-1]:
            return pivot + len(arr2)
        else:
            return search(arr1,0,len(arr1)-1,target)
            
