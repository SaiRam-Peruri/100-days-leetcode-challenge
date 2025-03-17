class Solution:
    def findMin(self, nums: List[int]) -> int:
        L=0
        R=len(nums)-1
        ans=float('inf')
        while L<=R:
            mid = L + (R-L)//2
            if nums[L]<nums[R]:
                return nums[L] if nums[L]<ans else ans
            if nums[mid]<nums[R]:
                if nums[mid]<ans:
                    ans=nums[mid]
                R=mid-1
            else:
                if nums[L]<ans:
                    ans=nums[L]
                L=mid+1
        return ans