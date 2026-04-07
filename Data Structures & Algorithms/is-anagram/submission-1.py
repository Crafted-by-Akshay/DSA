from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not s or not t or len(s) != len(t):
            return False

        counter = [0] *128

        for ch in s:
            counter[ord(ch)] +=1

        for ch in t:
            counter[ord(ch)] -=1
            if counter[ord(ch)] <0:
                return False

        return True