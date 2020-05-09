class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ## v1 24 ms
        jewels = set(J)
        count = 0
        for el in S:
            if el in jewels:
                count+=1
        return count

        # 24 ms
        jewels = set(J)
        return sum(S.count(j) for j in jewels)
        

        # fastes 24 ms
        jewels = set(J)
        return sum(1 for el in S if el in jewels)
        
        # 32ms with intwesection
        dic = {el: S.count(el) for el in set(S)}
        count = 0
        jewels = set(J)
        stones = set(dic.keys())
        inter = jewels.intersection(stones)
        for el in inter:
            count+= dic[el]
        return count
            