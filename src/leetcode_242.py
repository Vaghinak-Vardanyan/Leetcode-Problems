
# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        lookup_table: dict[str, int] = dict()
        
        for character in s:
            if character in lookup_table:
                lookup_table[character] += 1
            else:
                lookup_table[character] = 1
        
        for character in t:
            if character not in lookup_table:
                return False
            else:
                lookup_table[character] -= 1
                if lookup_table[character] == 0:
                    del lookup_table[character]
                
        return len(lookup_table) == 0