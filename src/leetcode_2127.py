from collections import deque


# 2127. Maximum Employees to Be Invited to a Meeting

class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        max_cycle: int = 0
        max_path: int = 0
        count: int = len(favorite)
        visited: list[bool] = [False] * count
        indegree: list[int] = [0] * count
        length: list[int] = [0] * count 
        roots = deque([], maxlen=count)

        for vertex in favorite:
            indegree[vertex] += 1

        for vertex, degree in enumerate(indegree):
            if not degree:
                roots.append(vertex)

        while roots:
            current = roots.pop()
            visited[current] = True
            length[favorite[current]] = max(length[current] + 1, length[favorite[current]])

            indegree[favorite[current]] -=1

            if not indegree[favorite[current]]:
                roots.append(favorite[current])

        for i in range(count):
            if not visited[i]:
                local_length = 0
                current = i
                while not visited[current]:
                    local_length += 1
                    visited[current] = True
                    current = favorite[current]
                
                if local_length == 2:
                    max_path += local_length + length[i] + length[favorite[i]]
                else:
                    max_cycle = max(max_cycle, local_length)

        return max(max_cycle, max_path)


    @staticmethod
    def fill_component_type(queue: deque, component_type: list[int], value):
        while queue:
            component_type[queue.pop()] = value


# # expected 3
# print(Solution().maximumInvitations([2, 2, 1, 2]))

# # expected 6
# print(Solution().maximumInvitations([1,0,0,2,1,4,7,8,9,6,7,10,8]))

# expected 11
print(Solution().maximumInvitations([1,0,3,2,5,6,7,4,9,8,11,10,11,12,10]))        

