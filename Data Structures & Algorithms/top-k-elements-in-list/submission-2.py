class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            dict[i] = dict.get(i,0) + 1
        n = len(nums)
        buckets = [[] for i in range(n+1)]

        for index,value in dict.items():
            buckets[value].append(index)
        result = []

        for i in range(n,0,-1):
            for num in buckets[i]:
                result.append(num)
            if len(result) == k:
                return result

        