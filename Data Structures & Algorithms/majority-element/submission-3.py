class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import random

        num = random.choice(nums)
        half = len(nums) // 2 + 1
        print(nums.count(num))
        print(half)
        while nums.count(num) < half:
            num = random.choice(nums)

        return num