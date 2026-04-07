class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        '''
        F(N,c) - > Maximum profit i can attain if i have  N items and c capacith
        '''
        def helper(n,capacity,profit,weight,dp):
            if capacity == 0:
                return 0
            if n == 0:
                return profit[0] if weight[0] <= capacity else 0
            
            if dp[n][capacity]!=-1:
                return dp[n][capacity]
            
            pick = helper(n-1,capacity-weight[n],profit,weight,dp) +profit[n] if weight[n]<=capacity else 0 
            not_pick = helper(n-1,capacity,profit,weight,dp)
            dp[n][capacity] = max(pick,not_pick)

            return dp[n][capacity]
        
        m = len(weight)
        n = capacity
        dp = [[-1]*(n+1) for i in range(m)]
        return helper(m-1,capacity,profit,weight,dp)
            
