class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maximum = 0

        for i in accounts:
            total = sum(i)
            maximum = max(maximum, total)

        return maximum