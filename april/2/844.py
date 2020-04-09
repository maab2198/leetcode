class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def parse(s):
            if "#" in s:
                i = s.index("#")
            else:
                return "".join(s)
            while i < len(s) and len(s):
                while len(s) and i < len(s) and s[i] == "#":
                    s.pop(i)
                    if i > 0:
                        s.pop(i-1)
                        i-=1
                i+=1
            return "".join(s)
        s = parse(list(S))
        t = parse(list(T))
        return True if s == t else False
