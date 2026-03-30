class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        num = nums[0]
        half = len(nums) // 2
        for number in nums:
            print(number, num, half)
            if number != num:
                num = number
                half = len(nums) // 2
            half -= 1
            if half < 0:
                break
        return num