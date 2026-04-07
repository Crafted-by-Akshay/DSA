from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not s or not t or len(s) != len(t):
            return False

        s_map = Counter(s)

        t_map = Counter(t)

        return s_map == t_map
        