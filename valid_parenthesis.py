# given a string, return true if all parenthesis in the string are valid or false is not 
# for example: "(){}" is valid but "({)}" is not valid

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else "#"
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack
