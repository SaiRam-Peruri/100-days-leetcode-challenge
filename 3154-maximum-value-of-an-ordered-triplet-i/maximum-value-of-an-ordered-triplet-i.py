class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        length=len(nums)
        maxi=0
        left_max=[]
        for r in nums:
            maxi=max(maxi,r)
            left_max+=[maxi]
        right_max=[]
        maxi=0
        for s in range(length):
            maxi=max(maxi,nums[length-s-1])
            right_max=[maxi]+right_max
        maxi=0
        for t in range(length-2):
            k=(left_max[t]-nums[t+1])*right_max[t+2]
            maxi=max(k,maxi)
        return maxi