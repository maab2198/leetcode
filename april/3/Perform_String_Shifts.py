class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if len(s) <=1:
            return s
        for pair in shift:
            k = pair[1] * (-1) if pair[0] else pair[1]
            s = s[k:] + s[:k]
        return s
