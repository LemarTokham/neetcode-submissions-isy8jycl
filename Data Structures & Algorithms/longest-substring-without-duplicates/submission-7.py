class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxS = 1
        seen = set()
        l = 0
        r = 0
        while r < len(s):
            if s[r] in seen:
                l += 1
                r = l 
                seen = set()
            seen.add(s[r])
            if len(seen) > maxS:
                maxS = len(seen)
            print(len(seen))
            r += 1

        return maxS
