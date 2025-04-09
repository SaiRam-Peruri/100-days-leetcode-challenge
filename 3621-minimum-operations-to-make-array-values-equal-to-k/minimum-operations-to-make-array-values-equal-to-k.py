class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for r in nums:
            if r>=k:
                continue
            else:
                return -1
        count=0
        nums=list(set(nums))
        for s in nums:
            if s>k:
                count+=1
        return count
        