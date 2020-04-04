class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n <= 1:
            return n
        groups = dict()
        for i in range(1,n+1):
            s = sum([int(k) for k in str(i)])
            if s in groups:
                groups[s] +=1
            else:
                groups[s] = 1
        l = list(groups.values())
        m = max(l)
        return l.count(m)
        