class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)>1:
            return ([0]*len(nums))
        elif nums.count(0)==1:
            a=0
            b=1
            for r in range(len(nums)):
                if nums[r]!=0:
                    b*=nums[r]
                else:
                    a=r
                    print(a)
            nums=[0]*len(nums)
            nums[a]=b
            return(nums)
        else:
            c=1
            d=[]
            for r in nums:
                c*=r
            for r in nums:
                d+=[c//r]
            return(d)