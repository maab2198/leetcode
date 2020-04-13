class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] !=9:
            return digits[:-1] + [digits[-1] + 1]
        i = str(int("".join(map(str,digits))) + 1)
        return [el for el in i]
