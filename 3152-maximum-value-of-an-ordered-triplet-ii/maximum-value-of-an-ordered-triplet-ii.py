class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        length=len(nums)
        left_max=[0]*length
        right_max=[0]*length
        for s in range(length-1):
            left_max[s+1]=max(left_max[s],nums[s])
            right_max[length-s-2]=max(right_max[length-s-1],nums[length-s-1])
        return max(0,max((left_max[i]-nums[i])*right_max[i] for i in range(1, length-1)))