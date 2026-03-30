class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result in nums:
                num_index = nums.index(result)
                if num_index in num_dict:
                    return [num_index, i]
                else:
                    num_dict[i] = nums[i]
