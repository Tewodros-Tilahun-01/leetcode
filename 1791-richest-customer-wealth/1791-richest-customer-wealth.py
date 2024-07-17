class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for person in accounts:
            person_wealth = 0
            for bank in person:
                person_wealth += bank
            max_wealth = max(person_wealth,max_wealth)
        return max_wealth