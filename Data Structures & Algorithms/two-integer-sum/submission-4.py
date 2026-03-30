class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            current_num = nums[i]
            numDict[current_num] = i
            

        for i in range(len(nums)):
            change = target - nums[i]
            if change in numDict:
                # Check for same index
                if numDict[change] == i:
                    continue
                return [i, numDict[change]]
