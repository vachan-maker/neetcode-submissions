class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums) #we are creating a set because the list can contain repeated digits
        longest  = 0
        for num in nums:
            if (num - 1) not in hashset:
                length = 1
                while num + length in hashset:
                    length += 1
                longest = max(longest,length)
        return longest