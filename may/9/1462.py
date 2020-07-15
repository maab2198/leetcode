class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        d = dict()
        for pair in prerequisites:
            if pair[0] in d:
                if pair[1] in d:
                    d[pair[1]] =  list(set(d[pair[1]] + [pair[0]] + d[pair[0]]))
                else:
                    d[pair[1]] = list(set([pair[0]] + d[pair[0]]))
            else:
                if pair[1] in d:
                    d[pair[1]] += [pair[0]]
                else:
                    d[pair[1]] = [pair[0]]
        res = []
        #print(d)
        for q in queries:
            if q[1] in d and q[0] in d[q[1]]:
                res.append(True)
            else:
                res.append(False)
        return res
