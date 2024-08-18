class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"
        st = set(nums)
        if len(st) == 1:
            return "equilateral"
        elif len(st) == 2:
            return 'isosceles'
        elif len(st) == 3:
            return 'scalene'
        return 'none'
        