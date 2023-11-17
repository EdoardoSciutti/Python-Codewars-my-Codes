import bisect

class BIT:
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & -i
        return res

def smaller(arr):
    sorted_arr = sorted(arr)
    result = []
    tree = BIT(len(arr))
    for num in reversed(arr):
        i = bisect.bisect_left(sorted_arr, num) + 1
        result.append(tree.query(i - 1))
        tree.update(i, 1)
    return result[::-1]