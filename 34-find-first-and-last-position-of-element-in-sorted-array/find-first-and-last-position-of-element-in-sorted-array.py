class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        L = 0
        R  = len(nums) - 1
        ans = -1
        LL = 0
        LR  = len(nums) - 1
        sol = -1
        while L <=R:
            mid = L + (R - L)//2
            if nums[mid]==target:
                ans = mid
                R = mid - 1
            elif nums[mid]>target:
                R = mid - 1
            else:
                L = mid + 1
        while LL <= LR:
            mid = LL + (LR - LL)//2
            if nums[mid]==target:
                sol = mid
                LL = mid + 1
            elif nums[mid]<target:
                LL = mid + 1
            else:
                LR = mid - 1
        return ans , sol