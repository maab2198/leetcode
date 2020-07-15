class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # dic = {el: S.count(el) for el in set(S)}
        # count = 0
        jewels = set(J)
        # stones = set(dic.keys())
        # inter = jewels.intersection(stones)
        # for el in inter:
        #     count+= dic[el]
#         for el in dic:
#             if el in jewels:
#                 count += dic[el]

        # count = 0
        # for el in S:
        #     if el in jewels:
        #         count+=1
        # return count
        # return sum([S.count(j) for j in jewels])
        return sum(1 for el in S if el in jewels)
        
