class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        end_res = 0
        stack = []

        for i in range(0, len(tokens)):
            if tokens[i] not in ["+", "*", "-", "/"]:
                stack.append(int(tokens[i]))
            else:
                left = stack.pop()
                right = stack.pop()

                match tokens[i]:
                    case "+":
                        stack.append(right + left)
                    case "-":
                        stack.append(right - left)
                    case "*":
                        stack.append(right * left)
                    case "/":
                        stack.append(int(right / left))
                    
        return stack[0]
