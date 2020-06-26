class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # write your code here
        counter = collections.Counter(tasks)
        max_length = max(counter.values())
        offset = 0
        for item in counter:
            if counter[item] == max_length:
                offset += 1
        return max(len(tasks), offset + (max_length - 1) * (n + 1))
