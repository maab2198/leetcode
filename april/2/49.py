class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for el in strs:
            s = "".join(sorted(el))
            if s in d:
                d[s].append(el)
            else:
                d[s] = [el]
        return d.values()