from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list)

        for s in strs:
            key = [0]*26
            for ch in s:
                key[ord(ch)- ord('a')] +=1

            anagram_map[tuple(key)].append(s)
        
        return list(anagram_map.values())


        
        
        
        ##################################
        #for s in strs:
        #    key = ''.join(sorted(s))
        #    anagram_map[key].append(s)

        #return list(anagram_map.values())

        # Time complexity
        # (N.KlogK)
        # Space complexity
        # O(N.K)

        ##################################
        