class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        d = {el: stones.count(el) for el in set(stones)}
        while True:
            m = max(d.keys())
            if d[m] > 1:
                d[m] -= 2
            elif d[m] == 1:
                if len(d.keys()) == 1:
                    return m
                x = m
                del d[m]
                m = max(d.keys())
                if not m:
                    return 0
                y = x - m
                d[y] = d[y] +1 if y in d else 1
                d[m] -= 1
            if not d[m]:
                del d[m]
            if not d:
                return 0
        return 0
