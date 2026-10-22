class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        minNumber = min(nums)
        maxNumber = max(nums)

        for i in range(minNumber,maxNumber+1):
            if i not in nums:
                return i
        return 0