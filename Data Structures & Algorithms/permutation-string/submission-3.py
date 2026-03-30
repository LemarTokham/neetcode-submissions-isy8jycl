class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Dict = {}
        for i in range(len(s1)):
            s1Dict[s1[i]] = 1 + s1Dict.get(s1[i], 0)

        l, r = 0, 0
        s1Copy = s1Dict
        while l < len(s2):
            if s2[l] in s1Copy: # found a letter in s2 which is in s1 - start window
                r = l
                s1Copy = s1Dict.copy()
                while r < len(s2) and s2[r] in s1Copy:
                    s1Copy[s2[r]] -= 1
                    if s1Copy[s2[r]] < 0: # subtracted too many times - invalid
                        break
                    r += 1
                    if r - l == len(s1): # found permutation
                        return True
            l += 1
        return False