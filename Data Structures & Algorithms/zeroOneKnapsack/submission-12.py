class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        items = len(weight)
        capacity = capacity

        dp = [[0]*(capacity+1) for i in range(items)]

        for i in range(items):
            dp[i][0] = 0 

        for c in range(capacity+1):
            if weight[0] <= c:
                dp[0][c] = profit[0]

        for i in range(1, items):
            for c in range(1, capacity+1):
                pick = profit[i] + dp[i-1][c-weight[i]] if c - weight[i] >= 0 else 0
                skip = dp[i-1][c]
                dp[i][c] = max(pick, skip)

        return dp[items-1][capacity]


