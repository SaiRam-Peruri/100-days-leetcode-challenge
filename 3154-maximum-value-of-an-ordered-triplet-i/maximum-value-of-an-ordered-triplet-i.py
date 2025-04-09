class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        length=len(nums)
        maxi=0
        for r in range(length):
            for s in range(r+1,length):
                for t in range(s+1,length):
                    total=(nums[r]-nums[s])*nums[t]
                    maxi=max(maxi,total)
        return maxi
