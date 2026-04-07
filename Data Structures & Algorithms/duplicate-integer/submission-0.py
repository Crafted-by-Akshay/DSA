class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        seen_map = set()

        for n in nums:
            if n in seen_map:
                return True
            seen_map.add(n)
        
        return False
        