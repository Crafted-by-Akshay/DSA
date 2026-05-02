class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        n = len(nums)
        ans = [0] * (2*n)

        for i in range(2*n):
            ans[i] = nums[i%n]
        
        return ans