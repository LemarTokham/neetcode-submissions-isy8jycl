class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict -> num: index
        numDict = {}
        for i in range(len(nums)):
            numDict[nums[i]] = i

        for i in range(len(nums)):
            res = target - nums[i]
            if res in numDict and i != numDict[res]:
                minIndex = min(i, numDict[res])
                maxIndex = max(i, numDict[res])
                return [minIndex, maxIndex]
        
