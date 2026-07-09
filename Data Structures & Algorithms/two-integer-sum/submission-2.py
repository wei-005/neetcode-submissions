class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums_dict = {}
        # res = []
        # for i, val in enumerate(nums):
        #     nums_dict[val] = i
        # for i in range(len(nums)):
        #     gap = target - nums[i]
        #     if gap in nums_dict and nums_dict[gap] != i:
        #         res.append(i)
        #         res.append(nums_dict[gap])
        #         break

        # return res

        nums_dict = {}

        for i, num in enumerate(nums):
            gap = target - num

            if gap in nums_dict:
                return [nums_dict[gap], i]

            nums_dict[num] = i


        