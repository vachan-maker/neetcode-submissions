class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listset = set(nums)
        return len(set(nums)) != len(nums)
        