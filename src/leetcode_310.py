
# 310. Minimum Height Trees

from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list: List[List[int]] = [list() for _ in range(n)]
        degrees: List[List] = [0] * n
        queue: deque = deque()
        
        if not edges:
            return [0]
        
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1
            
        for vertex, degree in enumerate(degrees):
            if degree == 1:
                queue.append(vertex)
                
        while n > 2:
            leaf_count = len(queue)
            n -= leaf_count
            for _ in range(leaf_count):
                current = queue.popleft()
                for neighbor in adj_list[current]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)


        return queue


print(Solution().findMinHeightTrees(11, [[0,1],[0,2],[2,3],[0,4],[2,5],[5,6],[3,7],[6,8],[8,9],[9,10]]))