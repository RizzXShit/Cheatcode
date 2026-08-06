class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        k = max(val/idx for idx,val in enumerate(accumulate(nums),1))
        return math.ceil(k)