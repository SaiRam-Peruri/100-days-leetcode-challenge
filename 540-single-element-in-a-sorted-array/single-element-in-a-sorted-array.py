class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        L=1
        R=n-1
        while L<=R:
            mid = L + (R - L)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if mid%2==1 and nums[mid]==nums[mid-1] or mid%2==0 and nums[mid]==nums[mid+1]:
                L= mid + 1
            else:
                R = mid -1