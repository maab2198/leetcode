class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not k:
            return num
        size = len(num) - k
        l = [None] * size
        top = 0
        for i in range(0,len(num)):
            digit = int(num[i])
            while top > 0 and k and l[top-1] > digit:
                top -=1
                k-=1
            if top < size:
                l[top] = digit
                top+=1
            else:
                k -=1
        while len(l) and not l[0]:
            l.pop(0)
        if not len(l):
            return "0"
        return "".join(map(str,l))

        
