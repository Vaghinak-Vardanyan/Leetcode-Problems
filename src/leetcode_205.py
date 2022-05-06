
# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapping: dict[str, str] = dict()
            
        # s -> t mapping
        for first, second in zip(s, t):
            if first not in mapping:
                mapping[first] = second
            else:
                if second != mapping[first]:
                    return False
        
        mapping.clear()
        
        # t -> s mapping                
        for first, second in zip(s, t):
            if second not in mapping:
                mapping[second] = first
            else:
                if first != mapping[second]:
                    return False
                
        return True


print(Solution().isIsomorphic(s = "bbbaaaba", t = "aaabbbba"))