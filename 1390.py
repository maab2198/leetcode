class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        s = 0
        for el in nums:
            divs_arr = self.printDivisors(el)
            if len(divs_arr) == 4:
                s+=sum(divs_arr)
        return s
    def printDivisors(self,n) :
        arr = []
        i = 1
        while i <= math.sqrt(n): 
            if (n % i == 0) : 
                if (n / i == i) : 
                    arr.append(i), 
                else : 
                    arr.append(i)
                    arr.append(int(n/i)) 
            i = i + 1
        return(arr)