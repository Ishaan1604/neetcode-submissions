class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        if len(s)%2 != 0:
            return False

        if s[0] not in symbols:
            return False
        stack = []
        for c in s:
            if c in symbols:
                stack.append(c)
            elif (not stack) or (c != symbols[stack.pop()]):
                return False
        
        if stack:
            return False

        return True
        
        
        

            

        
        

        