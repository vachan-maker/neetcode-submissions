class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        minNumber = 0
        maxNumber = len(nums)
        missing = 0
        for i in range(minNumber,maxNumber+1):
            if i not in nums:
                missing = i
        return missing