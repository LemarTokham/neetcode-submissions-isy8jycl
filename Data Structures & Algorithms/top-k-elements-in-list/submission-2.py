class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        # Create dictioanry for num : count
        for i in range(len(nums)):
            num = nums[i]
            numDict[num] = numDict.get(num, 0) + 1
        

        # Function to give us the max value in the dict 
        def findMaxInDict(numDict):
            maxVal = 0
            maxKey = 0
            for key, val in numDict.items():
                if val > maxVal:
                    maxVal = val
                    maxKey = key
            return maxKey
        
        result = []
        key = 0
        for i in range(k):
            key = findMaxInDict(numDict)
            result.append(key)
            numDict.pop(key)
        return result

            
        