class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        suffix = [0] * n
        prefix = [0] * n
        resNum = 1 # Keeps track of our calculations
        for i in range(n):
            if i == 0: # First number
                prefix[i] = resNum
                continue
            resNum = nums[i-1] * resNum
            prefix[i] = resNum
        resNum = 1 # Reset for new use with suffix
        for i in range(n - 1, -1, -1):
            if i == n-1: # Last number
                suffix[i] = resNum
                continue
            resNum = nums[i+1] * resNum
            suffix[i] = resNum
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        return res
        