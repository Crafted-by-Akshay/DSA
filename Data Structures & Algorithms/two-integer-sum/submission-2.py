class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2 or not nums:
            return[-1,-1]

        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return[seen[complement],i]
            
            seen[nums[i]] = i

        return [-1,-1]

        
        
        
        '''
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]
        
        return[-1,-1]

        # Time complexity : O(n^2)
        # Space complexity: O(1)
        '''