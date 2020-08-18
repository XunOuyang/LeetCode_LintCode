class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0 for i in range(num_people)]
        counter = 0
        while candies:
            for i in range(num_people):
                counter += 1
                if candies - counter >= 0:
                    res[i] += counter
                    candies -= counter
                else:
                    res[i] += candies
                    candies = 0
                    break
        return res
