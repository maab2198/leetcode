class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s[i] in t:
                ind = t.index(s[i]) +1
                t = t[ind:]
            else:
                return False
        return True