from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True

        if not s or not t or len(s)!= len(t):
            return False

        s_map = Counter(s)

        for c in t:
            if c not in s_map:
                return False
            
            s_map[c] -=1
            
            if s_map[c] == 0:
                del s_map[c]

        return len(s_map) == 0 
        

# Time complexity:
#------------------
# O(t+s) ~ O(2n) ~ O(n)

# Space complexity:
#------------------
# O(t) ~ O(n)