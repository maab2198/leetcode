class Solution:
    def isHappy(self, n: int) -> bool:
        square = set()
        while n not in square:
            square.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n ==1 
        