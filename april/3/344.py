class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) <=1:
            return s
        for i in range(0,len(s)//2):
            s[i], s[(i+1)*-1] = s[(i+1)*-1], s[i]
        """
        Do not return anything, modify s in-place instead.
        """
        
