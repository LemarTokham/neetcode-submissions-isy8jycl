class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        res = defaultdict(list) # creates a dict where empty keys "exist" with their vals being empty lists
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) # lists cannot be keys so convert to tuples

        return list(res.values())