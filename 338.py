class Solution:
    def countBits(self, num: int) -> List[int]:
        group = {2:[0,1,1,2]}
        prev = []
        el = 0
        c = 3
        while el < num+1:
            i = int(len(prev)/2) *(-1) if len(prev) > 0 else -2
            last = group[c-1][i:]
            prev = prev + last + list(map(lambda x:x+1,last))
            group[c] = prev
            el = 2**c
            c+=1
        res = []
        for key in group:
            res += group[key]
        return res[:num+1]