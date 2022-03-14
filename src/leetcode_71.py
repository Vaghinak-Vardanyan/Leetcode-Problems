
# 71. Simplify Path

class Solution:
    def simplifyPath(self, path: str) -> str:
        result: list[str] = []
        current: str
        index: int    
        while True:
            path = path.lstrip("/")
            index = path.find("/")
            
            if index != -1:
                current = path[:index]
                path = path[index:]
            elif path:
                current = path
                path = ""
            else:
                break

            if current == "..":
                if result:
                    result.pop()
            elif current != ".":
                result.append(current)

        return "/" + "/".join(result)
            

print(Solution().simplifyPath("/home/./"))