class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) -1
        A = []
        for i,num in enumerate(nums):
            A.append([num,i])
        A.sort()
        while left < right:
            if(A[left][0] + A[right][0] == target):
                return [min(A[left][1],A[right][1]),max(A[left][1],A[right][1])]
            elif(A[left][0] + A[right][0] > target):
                right = right - 1
            elif(A[left][0] + A[right][0] < target):
                left = left + 1
        return []
                

        