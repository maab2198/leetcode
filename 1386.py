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
                        
        