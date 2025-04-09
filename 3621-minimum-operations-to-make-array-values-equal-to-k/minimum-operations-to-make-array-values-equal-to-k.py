class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count=0
        nums=list(set(nums))
        for r in nums:
            if r>=k:
                if r>k:
                    count+=1
            else:
                return -1
        return count
        