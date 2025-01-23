class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        right = len(people) - 1
        left = 0
        boat = 0
        while left <= right:
            if people[left] + people[right] <= limit and left != right:
                left , right = left + 1 , right - 1
            else:
                right -= 1
            boat += 1
        return boat
    