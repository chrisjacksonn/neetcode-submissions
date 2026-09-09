class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        # key : value
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        # we'll be creating our own stack from the string
        for c in s: 
            if c in closeToOpen:
            # c is a closing bracket — check stack isn't empty AND its top matches c's required opener
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # append = push
                stack.append(c)
        # if the stack becomes empty, return True
        return True if not stack else False
