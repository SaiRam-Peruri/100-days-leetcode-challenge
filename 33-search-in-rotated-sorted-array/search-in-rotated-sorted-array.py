class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <=R:
            mid = L + (R - L)//2
            if nums[mid]==target:
                return mid
            #Left Half id Sorted
            if nums[L]<=nums[mid]:
                if nums[L]<=target<=nums[mid]:
                    R=mid-1 
                else:
                    L=mid+1
            #Right Half is Sorted
            else:
                if nums[mid]<=target<=nums[R]:
                    L=mid+1
                else:
                    R=mid-1
        return -1