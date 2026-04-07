class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        items, capacity = len(profit), capacity
        dp = [0] * (capacity + 1)

        # Fill the first row to reduce edge cases
        for c in range(capacity + 1):
            if weight[0] <= c:
                dp[c] = profit[0]

        for i in range(1, items):
            curRow = [0] * (capacity + 1)
            for c in range(1, capacity + 1):
                skip = dp[c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[c - weight[i]]
                curRow[c] = max(include, skip)
            dp = curRow
        return dp[-1]


