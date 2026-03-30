class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        # {num:index}
        for i in range(len(nums)):
            numDict[nums[i]] = i
        
        for i in range(len(nums)):
            res = target - nums[i]
            if res in numDict and i != numDict[res]:
                return [i, numDict[res]] if i < numDict[res] else [numDict[res], i]