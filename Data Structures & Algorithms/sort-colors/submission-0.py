class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3

        for number in nums:
            if number == 0:
                count[0] += 1
            elif number == 1:
                count[1] += 1
            else:
                count[2] += 1
        number = 0
        index =0
        for c in count:
            for r in range(c):
                nums[index] = number
                index +=1
            number += 1


