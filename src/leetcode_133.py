
# 133. Clone Graph

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors: Optional[list['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Optional[Node]:
        visited: dict[int, Node] = {}
        
        def cloneInternal(node: Node, current: Node):

            for vertex in node.neighbors:
                if vertex.val not in visited:
                    visited[vertex.val] = Node(vertex.val)
                    cloneInternal(vertex, visited[vertex.val])
                
                current.neighbors.append(visited[vertex.val])

        if not node:
            return None

        copied = Node(node.val)
        visited[copied.val] = copied
        cloneInternal(node, copied)
        return copied


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]


Solution().cloneGraph(node1)