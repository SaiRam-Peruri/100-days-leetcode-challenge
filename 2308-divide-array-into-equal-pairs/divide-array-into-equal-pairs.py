class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        length=len(nums)
        a=[0]*(max(nums)+1)
        for r in nums:
            a[r]=a[r]+1
        count=0
        for s in a:
            if s%2==0:
                count+=s
        return True if count==length else False