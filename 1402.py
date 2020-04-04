class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        max_sum = max(satisfaction)
        n = len(satisfaction)
        satisfaction.sort()
        if max_sum <= 0:
            return 0
        k = []
        while len(satisfaction) > 0:
            curr_sum, max_sum = 0,0
            n = len(satisfaction)
            for i in range(0,n):
                curr_sum += satisfaction[i]*(i+1)
                # if curr_sum < 0:
                #     curr_sum = 0
                if max_sum < curr_sum:
                    max_sum = curr_sum
            k.append(max_sum)
            satisfaction.pop(0)
        return max(k)
        