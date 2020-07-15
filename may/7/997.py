class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        people = set(pair[0] for pair in trust)
        trusted = {}
        if not len(trust):
            return 1 if N ==1 else -1
        for pair in trust:
            if pair[1] not in people:
                trusted[pair[1]] = (trusted[pair[1]] + 1) if pair[1] in trusted else 1
        ans = -1
        for key in trusted:
            if trusted[key] == N-1:
                ans = key if ans ==-1 else -1
        return ans
        # if not len(trust):
        #     return 1 if N ==1 else -1
        # for pair in trust:
        #     people.add(pair[0])
        #     if pair[1] not in trusted:
        #         trusted[pair[1]] = 1
        #     else:
        #         trusted[pair[1]] +=1
        #     if pair[0] in trusted:
        #         del trusted[pair[0]]
        # # print(trusted)
        # ans = -1
        # for key in trusted:
        #     if trusted[key] == N-1 and key not in people:
        #         ans = key if ans ==-1 else -1
        # return ans
