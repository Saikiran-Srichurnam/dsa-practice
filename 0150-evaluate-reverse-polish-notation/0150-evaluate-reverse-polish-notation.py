class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                val1 = stack.pop()
                val2 = stack.pop()

                if token == "+":
                    stack.append(val2+val1)
                elif token == "-":
                    stack.append(val2-val1)
                elif token == "*":
                    stack.append(val1 * val2)
                else:
                    value = math.trunc(val2 / val1)
                    stack.append(value)
            
        return stack[-1]
