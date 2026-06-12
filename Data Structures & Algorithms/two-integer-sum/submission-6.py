class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {} #val = key, index = element

        for i, val in enumerate(nums):
            ht[val] = i
        
        i1, i2 = 0, 0
        for i, val in enumerate(nums):
            complement = target - val
            if complement in ht and ht[complement] != i:
                return [i, ht[complement]]
        
        return []
