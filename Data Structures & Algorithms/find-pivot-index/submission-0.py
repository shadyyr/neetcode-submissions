class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #find the total sum of the array
        total = sum(nums)

        lhs = 0
        for idx, val in enumerate(nums):
            rhs = total - lhs - val
            if lhs == rhs:
                return idx
            lhs += val
        return -1