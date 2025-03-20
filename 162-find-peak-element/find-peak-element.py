class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[length-1]>nums[length-2]:
            return length-1
        L = 1
        R = length-2
        while L<=R:
            mid = L + (R - L)//2
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid
            elif nums[mid]>nums[mid-1]:
                L= mid + 1
            else:
                R = mid - 1
        return -1