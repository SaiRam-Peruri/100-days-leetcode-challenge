class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        while len(nums)>=0:
            if len(set(nums))==len(nums):
                return count
            else:
                nums=nums[3:]
                count+=1
        