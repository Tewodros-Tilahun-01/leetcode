class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 1) 
        sum = 0
        for booking in bookings:
            res[booking[0] - 1] += booking[2]
            res[booking[1]] -= booking[2]
        for i in range(n):
            sum += res[i]
            res[i] = sum
        res.pop()
        return res