class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        maxCount = 1 # will store how many r moves there are before left moves
        seen = set()
        count = 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                count += 1
                continue
            seen.remove(s[l])
            l += 1
            maxCount = max(count, maxCount)
            count -=1

        return max(maxCount, count)