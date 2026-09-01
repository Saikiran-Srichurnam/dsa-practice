class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # result = ""
        # count = 0
        # for ch in s:
        #     if ch == "(":
        #         count += 1
        #         if count > 1:
        #             result += ch
        #     else:
        #         count -= 1
        #         if count > 0:
        #             result += ch
        
        # return result

        # using stack 
        stack = []
        res = ""
        for i in range(len(s)):
            if s[i] == "(":
                if len(stack) > 0:
                    res += s[i]
                stack.append(s[i])
            elif s[i] == ")":
                if len(stack) > 1:
                    res += s[i]
                stack.pop()
        return res