class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)>1:
            return ([0]*len(nums))
        elif nums.count(0)==1:
            index=0
            product=1
            for r in range(len(nums)):
                if nums[r]!=0:
                    product*=nums[r]
                else:
                    index=r
            nums=[0]*len(nums)
            nums[index]=product
            return(nums)
        else:
            final_product=1
            final_list=[]
            for r in nums:
                final_product*=r
            for r in nums:
                final_list+=[final_product//r]
            return(final_list)