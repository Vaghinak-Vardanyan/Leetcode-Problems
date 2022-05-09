
# 207. Course Schedule

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0 -> not visited, 1 -> in process, 2 -> visited
        colors: List[int] = [0] * numCourses
        adj_list: List[List[int]] = [[] for _ in range(numCourses)]
        
        for end, start in prerequisites:
            adj_list[start].append(end)
    
    
        for vertex in range(numCourses):
            if colors[vertex] == 0 and self.containsCycle(vertex, colors, adj_list):
                return False
            
        return True
            
            
    def containsCycle(self, vertex: int, colors: List[int], adj_list: List[List[int]]) -> bool:
        colors[vertex] = 1
        for neighbor in adj_list[vertex]:
            if colors[neighbor] == 1:
                return True
                        
            if colors[neighbor] == 0 and self.containsCycle(neighbor, colors, adj_list):
                return True    
                
        colors[vertex] = 2    
        return False


print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))