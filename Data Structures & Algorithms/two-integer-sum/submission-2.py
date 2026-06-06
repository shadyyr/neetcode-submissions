class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make empty hashmap
        ht = {}

        for i, val in enumerate(nums):
            ht[val] = i

        for i, val in enumerate(nums):
            complement = target - val
            if complement in ht and ht[complement] != i:
                return [i, ht[complement]]