
# 210. Course Schedule II

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 0 -> not visited, 1 -> in process, 2 -> visited
        colors: List[int] = [0] * numCourses
        adj_list: List[List[int]] = [[] for _ in range(numCourses)]
        topology: List[int] = []
        
        for end, start in prerequisites:
            adj_list[start].append(end)
    
    
        for vertex in range(numCourses):
            if colors[vertex] == 0 and self.containsCycle(vertex, colors, adj_list, topology):
                return []
            
        return reversed(topology)
            
            
    def containsCycle(self, vertex: int, colors: List[int], adj_list: List[List[int]], topology: List[int]) -> bool:
        colors[vertex] = 1
        for neighbor in adj_list[vertex]:
            if colors[neighbor] == 1:
                return True
                        
            if colors[neighbor] == 0 and self.containsCycle(neighbor, colors, adj_list, topology):
                return True    
                
        topology.append(vertex)        
        colors[vertex] = 2    
        return False

