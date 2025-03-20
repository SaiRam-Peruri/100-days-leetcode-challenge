class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        L=0
        R=x
        ans=0
        while L<=R:
            mid= L+ (R-L)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                R=mid-1
            else:
                ans=mid
                L=mid+1
        return ans