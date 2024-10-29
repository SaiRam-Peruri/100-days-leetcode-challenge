class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        a=len(nums)
        b=[]
        c=[]
        if len(nums)==1:
            return nums[0]
        if len(nums)>1:
            for r in nums:
                if r<0:
                    b+=[r]
                else:
                    c+=[r]
            if len(b)==0:
                d=None
            else:
                d=b[0]
                if len(b)>1:
                    for r in range(0,len(b)-1):
                        if d>b[r+1]:
                            continue
                        else:
                            d=b[r+1]
            if len(c)==0:
                e=None
            else:
                e=c[0]
                if len(c)>1:
                    for r in range(0,len(c)-1):
                        if e<c[r+1]:
                            continue
                        else:
                            e=c[r+1]
        if d is not None and e is not None:
            if d*(-1)<e:
                return d
            else:
                return e
        if d is None:
            return e
        if e is None:
            return d


        
