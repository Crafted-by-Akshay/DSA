from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if not s or not t or len(s)!= len(t):
            return False

        s_map = Counter(s)

        for c in t:
            if c in s_map:
                s_map[c]-=1
                if s_map[c] == 0:
                    del s_map[c]
            else:
                return False
        
        return True