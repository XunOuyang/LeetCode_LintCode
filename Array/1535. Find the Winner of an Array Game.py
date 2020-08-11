class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if not arr:
            return -1
        if k >= len(arr):
            return max(arr)
        k = min(k, len(arr))
        i = 1
        while True:
            temp = k
            pointer = 1
            flag = False
            while temp:
                if i == len(arr):
                    i = 1
                if i < len(arr) and arr[0] > arr[i]:
                    i += 1
                    temp -= 1
                else:
                    arr[0], arr[i] = arr[i], arr[0]
                    pointer = i + 1
                    flag = True
                    break
            if not temp and not flag:
                return arr[0]
        return -1
