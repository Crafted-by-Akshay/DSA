class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        n = len(nums)

        result_array = [0] * (2*n)

        for i in range(2*n):
            result_array[i] = nums[i%n]

        return result_array


"""

Mental model
a % b

means:

“Take a, divide by b, keep the remainder.”

So:

i % n

means:

“Take the changing index i, wrap it into the range 0 to n-1.”

That’s exactly what you want for cycling through an array.

Concrete example

Say:

n = 3

Then:

0 % 3 = 0
1 % 3 = 1
2 % 3 = 2
3 % 3 = 0
4 % 3 = 1
5 % 3 = 2

Pattern:

0,1,2,0,1,2...
"""
