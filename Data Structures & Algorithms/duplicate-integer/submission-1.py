class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDict = {}
        for i in range(len(nums)):
            if nums[i] in numDict.values():
                return True
            else:
                numDict[i] = nums[i]
        return False