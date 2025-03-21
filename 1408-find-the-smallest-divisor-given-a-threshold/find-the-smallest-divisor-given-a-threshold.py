class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        L=1
        R=max(nums)
        ans=threshold
        while L<=R:
            target=0
            mid = L + (R - L)//2
            for r in nums:
                if r%mid!=0:
                    target+=(r//mid) + 1
                else:
                    target+=(r//mid)
            if target<=threshold:
                ans=mid
                R=mid-1
            else:
                L = mid+1
        return ans