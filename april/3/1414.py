class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        n1, n2 = 0, 1
        count = 0
        max_fib = k
        fib = [n1,n2]
        i = 2
        check = k
        if k == 1:
            return 1
        else:
            while fib[i-1] + fib[i-2] <= max_fib:
                fib.append(fib[i-1] + fib[i-2])
                if k % fib[i-1] ==0:
                    check = k //fib[i-1]
                i+=1
        # print(fib)
        index = len(fib) 
        if k in fib:
            return 1
        count = 0
        while k!=0:
            k -= max(fib[:index])
            count +=1
            if k not in fib[:index]:
                while fib[index-1] > k:
                    index -= 1
            else:
                count +=1
                break
        # print(count)
        return min(count,check)
