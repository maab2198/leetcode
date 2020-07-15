from itertools import permutations

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
    #     comb = combinations_with_replacement([1, 0], k)
    #     a = [1]*k + [0]*k
    #     perm = permutations(a, k)
    #     l = set(perm)
    #     print(len(s))
    #     for i in l:
    #         line = "".join(map(str,i))
    #         #print(line)
    #         if s.find(line) == -1:
    #             return False
    #     return True

        set_t = set()
        for i in range(k, len(s)+1) :
            set_t.add(s[i-k:i])
            #print(set_t)
        return len(set_t) == 2**k
