class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        diff = 0 
        seats.sort()
        students.sort()
        for i in range(len(seats)):
           diff += abs(seats[i]-students[i])
        return diff