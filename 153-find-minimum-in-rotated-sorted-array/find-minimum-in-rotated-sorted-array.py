class Solution:
    def findMin(self, nums: List[int]) -> int:
        L=0
        R=len(nums)-1
        ans=float('inf')
        while L<=R:
            mid = L + (R-L)//2
            if nums[mid]<nums[R]:
                ans=min(nums[mid],ans)
                R=mid-1
            else:
                ans=min(nums[L],ans)
                L=mid+1
        return ans