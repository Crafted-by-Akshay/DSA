class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) ==1:
            return False

        seen_map = set()

        for n in nums:
            if n in seen_map:
                return True
            seen_map.add(n)

        return False

# Time Complexity : O(n)
# Space Complexity : O(n)