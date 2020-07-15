class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # if num <=0:
        #     return False
        # if num == 1:
        #     return True
        # def searcher(l,r,num):
        #     while l<=r:
        #         mid = (l+r)//2
        #         if mid*mid == num:
        #             return True
        #         elif mid*mid < num:
        #             return searcher(mid+1,r,num)
        #         else:
        #             return searcher(l,mid-1,num)
        # return searcher(1,num//2,num)
        if num <=0:
            return False
        a = num **0.5
        return a == int(a)

        # nice )))
        # def isPerfectSquare(self, num: int) -> bool:
        # l = 1
        # r = num
        # while(r >= l):
        #     mid = int((l + r) / 2)
        #     if mid ** 2 == num:
        #         return True
        #     elif mid ** 2 > num:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return False
        
