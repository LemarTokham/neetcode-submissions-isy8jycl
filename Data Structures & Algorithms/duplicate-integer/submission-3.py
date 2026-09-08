class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # convert to set, if set has same size as array, no dupes
        return len(set(nums)) != len(nums)