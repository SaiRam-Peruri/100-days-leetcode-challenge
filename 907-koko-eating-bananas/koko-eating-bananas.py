class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L=1
        R=max(piles)
        ans = R
        while L<=R:
            mid = L + (R - L)//2
            bananas=0
            for r in piles:
                if r%mid==0:
                    bananas+= r//mid
                else:
                    bananas+= (r//mid) + 1
            if bananas<=h:
                ans = mid
                R = mid-1
            else:
                L=mid+1
        return ans