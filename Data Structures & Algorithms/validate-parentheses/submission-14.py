class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for char in s:
            if char == "(":
                queue.append(")")
            elif char == ")":
                if len(queue) == 0:
                    return False
                if queue.pop() != ")":
                    return False
            
            if char == "[":
                queue.append("]")
            elif char == "]":
                if len(queue) == 0:
                    return False
                if queue.pop() != "]":
                    return False

            if char == "{":
                queue.append("}")
            elif char == "}":
                if len(queue) == 0:
                    return False
                if queue.pop() != "}":
                    return False
        
        return True if len(queue) == 0 else False