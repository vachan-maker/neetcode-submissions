# Wrong Solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        minNumber = min(nums)
        maxNumber = max(nums) # the problem is that we need to check the length of the list and not the maximum number because max number can be absent from the list

        for i in range(minNumber,maxNumber+1):
            if i not in nums:
                return i
        return 0
