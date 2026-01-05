class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            divisor_list = set()
            div_sum = 0
            for x in range(1,int(num**0.5)+1):
                if (num%x) == 0:
                    divisor = num//x
                    divisor_list.add(x)
                    divisor_list.add(divisor)
                    div_sum+=x
                    div_sum+=divisor
            if len(divisor_list) == 4:
                result+=div_sum
        return result
