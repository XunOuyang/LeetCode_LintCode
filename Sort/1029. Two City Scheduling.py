class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:(x[0]-x[1]))
        res = 0
        length = len(costs)
        for i, cost in enumerate(costs):
            if i < length / 2:
                res += cost[0]
            else:
                res += cost[1]
        return res
