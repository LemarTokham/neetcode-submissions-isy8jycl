class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        res = 0
        a = 0
        b = 0
        for i in range(len(tokens)):
            if tokens[i] == '+' or tokens[i] == '-' or tokens[i] == '*' or tokens[i] == '/':
                if len(stack) >= 2:
                    print(stack)
                    b = int(stack.pop())
                    a = int(stack.pop())
                if tokens[i] == '+':
                    res = int(a + b)
                    stack.append(res)
                    a = 0
                    b = 0
                elif tokens[i] == '-':
                    res = int(a - b)
                    stack.append(res)
                    a = 0
                    b = 0
                elif tokens[i] == '*':
                    res = int(a * b)
                    stack.append(res)
                    a = 0
                    b = 0
                elif tokens[i] == '/':
                    res = int(a / b)
                    stack.append(res)
                    a = 0
                    b = 0
            else:
                stack.append(tokens[i])
        return int(res)