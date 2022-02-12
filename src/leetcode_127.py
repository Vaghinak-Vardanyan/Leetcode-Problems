
# 127. Word Ladder

from typing import List
from collections import defaultdict
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        length: int = len(beginWord)
        word_by_generic: defaultdict = defaultdict(list)
        queue: deque[tuple[str, int]] = deque([(beginWord, 1)])
        visited: dict = { beginWord: True }

        for word in wordList:
            for i in range(length):
                word_by_generic[word[:i] + "*" + word[i+1:]].append(word)

        while queue:
            current_word, level = queue.popleft()
            for i in range(length):
                generic_word = current_word[:i] + "*" + current_word[i+1:]

                for word in word_by_generic[generic_word]:

                    if word == endWord:
                        return level + 1

                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                
                word_by_generic[generic_word] = []
        
        return 0


print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))