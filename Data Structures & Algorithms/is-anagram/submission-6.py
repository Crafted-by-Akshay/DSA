from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t or len(s)!= len(t):
            return False

        char_map = Counter(s)

        for c in t:
            if c not in char_map:
                return False
            
            char_map[c] -=1
            
            if char_map[c] == 0:
                del char_map[c]

        return True if len(char_map) == 0 else False

# Time complexity
# O(2*26) ~ O(26)

# Space complexity
# O(26)

            