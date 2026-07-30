# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # res = [[] * len(pairs)]
        # res[0] = pairs
        # for i in range(1, len(pairs)):
        #     for j in range(len(pairs) - 1):
        #         if res[i][j][0] <= res[i][j + 1][0]:
        #             continue
        #         else:
        #             res[i][j][0], res[i][j + 1][0] = res[i][j + 1][0], res[i][j][0]
        #     continue

        # return res
        res = []

        for i in range(len(pairs)):
            j = i

            while j > 0 and pairs[j - 1].key > pairs[j].key:
                pairs[j - 1], pairs[j] = pairs[j], pairs[j - 1]
                j -= 1

            res.append(pairs[:])

        return res
        