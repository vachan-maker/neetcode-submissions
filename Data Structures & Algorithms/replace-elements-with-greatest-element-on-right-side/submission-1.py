class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        ans = [0] * length
        for i in range(len(arr)):
            maxNumber = -1
            for j in range(i+1,len(arr)):
                maxNumber = max(maxNumber,arr[j])
            ans[i] = maxNumber
        return ans