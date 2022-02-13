
# 2135. Count Words Obtained After Adding a Letter

from typing import List

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        result: int = 0
        codes: set[int] = set()
        ord_a: int = ord("a")

        for word in startWords:
            codes.add(self.get_word_code(word))

        for word in targetWords:
            word_code: int = self.get_word_code(word)

            for character in word:
                if word_code ^ (1 << (ord(character) - ord_a)) in codes:
                    result += 1
                    break

        return result
            

    def get_word_code(self, word: str) -> int:
        word_code: int = 0
        ord_a = ord("a")

        for character in word:
            word_code ^= 1 << (ord(character) - ord_a)

        return word_code

print(Solution().wordCount(["ant","act","tack"], ["tack","act","acti"]))