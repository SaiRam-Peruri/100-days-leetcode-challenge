class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        L=0
        R=len(arr)
        while L<R:
            mid = L + (R - L)//2
            if arr[mid] - mid - 1 < k:
                L = mid + 1
            else:
                R = mid
        return R + k