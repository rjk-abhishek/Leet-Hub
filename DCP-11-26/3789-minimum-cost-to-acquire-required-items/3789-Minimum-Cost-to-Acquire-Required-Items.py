class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1, need2)
        pair_cost = min(cost1 + cost2, costBoth)
        total_cost = common * pair_cost
        rem1 = need1 - common
        rem2 = need2 - common
        total_cost += rem1 * min(cost1, costBoth)
        total_cost += rem2 * min(cost2, costBoth)
        return total_cost