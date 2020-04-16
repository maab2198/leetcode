class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for el in s:
            if el in d:
                d[el]+=1
            else:
                d[el] =1
        for i in range(len(s)):
            if d[s[i]] ==1:
                return i
        return -1
