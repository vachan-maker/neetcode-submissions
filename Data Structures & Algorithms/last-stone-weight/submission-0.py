class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            stones.sort()
            x_index = len(stones)-1
            y_index= len(stones)-2
            x = stones[x_index]
            y = stones[y_index]
            if(x==y):
                stones.pop(x_index)
                stones.pop(y_index)
            elif (y<x):
                stones[y_index] = x-y
                stones.pop(x_index)
        if (len(stones)==1):
            return stones[0]
        else:
            return 0

        