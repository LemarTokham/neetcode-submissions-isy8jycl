class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0: # a bracket is pair, so for vaid pairs, we must have even pairs
            return False
        for i in range(len(s)):
            # pushing open brackets to stack
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False;
                # compare closed bracket with top of stack, if they are same type, then valid bracket
                if s[i] == ')':
                    if stack[-1] == '(':
                        stack.pop() # valid bracket, therefore remove it to consider next bracket
                    else:
                        return False
                elif s[i] == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif s[i] == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        return (len(stack) == 0)


