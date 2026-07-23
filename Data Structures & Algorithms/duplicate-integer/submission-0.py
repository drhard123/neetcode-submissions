class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            pass
        else:
            flag = True
        return flag

        
        