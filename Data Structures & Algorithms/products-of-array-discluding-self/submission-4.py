class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prod = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            result.append(prod)
            prod = 1

        return result