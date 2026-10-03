from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if (not s or not t) or len(s)!= len(t):
            return False

        s_map = Counter(s)
        #print('s_map',s_map)

        for ch in t:
            if ch not in s_map:
                return False
            s_map[ch] -=1
            if s_map[ch] == 0:
                del s_map[ch]
        
        return True if not s_map else False
