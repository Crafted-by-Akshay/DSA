class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        items, capacity = len(profit), capacity
        prev_row = [0] * (capacity + 1)

        # Fill the first row to reduce edge cases
        for c in range(capacity + 1):
            if weight[0] <= c:
                prev_row[c] = profit[0]

        for i in range(1, items):
            curRow = [0] * (capacity + 1)
            for c in range(1, capacity + 1):
                skip = prev_row [c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + prev_row[c - weight[i]]
                curRow[c] = max(include, skip)
            prev_row  = curRow
        return prev_row [-1]

