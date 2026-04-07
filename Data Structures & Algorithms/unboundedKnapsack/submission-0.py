class Solution:
    def helper(self,index,capacity,weight,profits,memo) -> int:
        if capacity == 0 or index == 0 :
            return 0
        if memo[index][capacity]!=-1:
            return memo[index][capacity]
        
        skip =  self.helper(index-1,capacity,weight,profits,memo)  
        pick = 0
        new_capacity = capacity - weight[index-1]
        if new_capacity >=0:
            pick = self.helper(index,new_capacity,weight,profits,memo) + profits[index-1]
        
        memo[index][capacity] = max(pick,skip)
        return memo[index][capacity]

    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = [[-1]*(capacity+1) for i in range(len(profit)+1)]
        n = len(profit)
        return self.helper(n,capacity,weight,profit,memo)  
        
