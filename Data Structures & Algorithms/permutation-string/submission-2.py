class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = {}
        for i in range(len(s1)): # count frequencies of each let
            s1_dict[s1[i]] = 1 + s1_dict.get(s1[i], 0)

        l, r = 0, 0
        temp_dict = {}
        while l < len(s2) and r < len(s2):
            if s2[r] not in s1_dict:
                l += 1
                r = l
                temp_dict = {}
                continue
            temp_dict[s2[r]] = 1 + temp_dict.get(s2[r], 0)
            if r - l >= len(s1) - 1:
                if temp_dict == s1_dict:
                    return True
                l += 1
                r = l
                temp_dict = {}
                continue
            
            r+= 1
        
        return False
