class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new = set(nums)
        for i in new:
            if nums.count(i) == 1:
                return i
        # l = []
        # for i in nums:
        #     if i not in l:
        #         if nums.count(i) == 1:
        #             return i
        # return None
        