class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [[temperatures[0], 0]]
        for i in range(1, len(temperatures)):
            print(stack[-1])
            while temperatures[i] > stack[-1][0]:
                print("hit")
                # pop from stack
                temp = stack.pop(-1) # an array of [temp, index]
                res[temp[1]] = i - temp[1]
                if not stack:
                    break
            stack.append([temperatures[i], i])
        return res