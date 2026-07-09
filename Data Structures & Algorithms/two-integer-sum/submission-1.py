class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        res = []
        for i, val in enumerate(nums):
            # if val not in nums_dict:
            nums_dict[val] = i
            # else:
            #     nums_dict
        for i in range(len(nums)):
            gap = target - nums[i]
            if gap in nums_dict and nums_dict[gap] != i:
                res.append(i)
                res.append(nums_dict[gap])
                break

        return res


        