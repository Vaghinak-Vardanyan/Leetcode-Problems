
# 1160. Find Words That Can Be Formed by Characters

from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        result: int = 0
        chars_available: dict[str, int] = dict()
            
        for char in chars:
            if char not in chars_available:
                chars_available[char] = 1
            else:
                chars_available[char] += 1
        
        for word in words:
            if self.canBeFormed(word, chars_available):
                result += len(word)
        
        return result
    
    
    def canBeFormed(self, word, chars_available: 'dict[str, int]') -> bool:
        word_chars: dict[str, int] = dict()
        for char in word:
            if char not in chars_available:
                return False

            if char not in word_chars:
                word_chars[char] = 1
            else:
                word_chars[char] += 1

            if chars_available[char] < word_chars[char]:
                return False
                
        return True