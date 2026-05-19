class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        n = len(nums)

        result_array = [0] * (2*n)

        for i in range(2*n):
            result_array[i] = nums[i%n]

        return result_array
        