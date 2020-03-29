class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = dict()
        variants = 2 *n
        for seat in reservedSeats:
            if seat[0] in seats:
                seats[seat[0]].append(seat[1])
            else:
                seats[seat[0]] = [seat[1]]
        for row in seats:
            arr = seats[row]
            left = True
            right = True
            center = True
            for j in range(0,len(arr)):
                left = False if arr[j] >= 2 and arr[j] <= 5 else left
                right = False if arr[j] >= 6 and arr[j] <= 9 else right
                center = False if arr[j] >= 4 and arr[j] <= 7 else center
            if left and right:
                pass
            elif center or right or left:
                variants -=1
            else:
                variants -=2
        return variants

# faster solution
# class Solution:
#     def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
#         X = {}
        
#         for i, j in reservedSeats:
#             if j not in {1, 10}:
#                 if i in X:
#                     X[i].add(j)
                    
#                 else:
#                     X[i] = {j}
#         m = (n - len(X)) * 2
#         for x in X.values():
#             a = not (2 in x or 3 in x)
#             b = not (4 in x or 5 in x)
#             c = not (6 in x or 7 in x)
#             d = not (8 in x or 9 in x)
            
#             m += 2 if a and b and c and d else \
#                  1 if a and b or b and c or c and d else \
#                  0
#         return m
                        
        
                        
        