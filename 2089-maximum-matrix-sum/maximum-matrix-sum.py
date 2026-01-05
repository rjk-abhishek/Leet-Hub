class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_count = 0
        y = float('inf')
        result = 0
        for num in matrix:
            for x in num:
                av = abs(x)
                result += av
                if x < 0:
                    neg_count+=1
                y = min(y, av)
        if (neg_count%2) == 0:
            return result
        else:
            return result - 2 * abs(y)