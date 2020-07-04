class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        res = []
        stack = []
        while N:
            N -= 1
            temp = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    temp[i] = 1
                else:
                    temp[i] = 0
            if cells == temp:
                break
            if temp in res and stack:
                index = res.index(temp)
                diff = stack[index] - N
                N = N % diff
            res.append(temp)
            stack.append(N)
            cells = temp
        return cells
