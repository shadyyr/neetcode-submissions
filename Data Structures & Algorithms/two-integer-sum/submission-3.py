class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make empty hashmap
        ht = {}

        ##key = value, value = index
        for i, val in enumerate(nums):
            ht[val] = i

        #calculate complement, if in ht, return list
        for i, val in enumerate(nums):
            complement = target - val
            if complement in ht and ht[complement] != i:
                return [i, ht[complement]]