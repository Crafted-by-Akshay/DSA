class Solution:
    def backtracking(self,n,capacity,profit,weight,dp):
        if capacity ==0:
            return 0 
        if n == 0:
            return profit[0] if weight[0]<=capacity else 0
        if dp[n][capacity]!=-1:
            return dp[n][capacity]
        
        pick = profit[n] + self.backtracking(n-1,capacity-weight[n],profit,weight,dp) if capacity-weight[n]>=0 else 0
        skip = self.backtracking(n-1,capacity,profit,weight,dp)
        
        dp[n][capacity] = max(pick,skip)
        return dp[n][capacity]

    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        items = len(weight)
        bag_size = capacity+1
        dp = [[-1]*bag_size for i in range(items)]

        return self.backtracking(items-1,bag_size-1,profit,weight,dp)



