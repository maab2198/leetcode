class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        s = -1 if x < 0 else 1
        x = abs(x)
        while x!=0:
            res =res*10 + x%10
            x = x //10
        return res*s*(res < 0x7FFFFFFF)
