class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        if n <= 1:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return memo[n]