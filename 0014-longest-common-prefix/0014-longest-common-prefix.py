class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=sorted(strs)
        b=a[0]
        c=len(strs)
        d=""
        for r in range(0,len(b)):
            count=0
            for s in range(c):
                if b[r]==a[s][r]:
                    count+=1
            if count==c:
                d+=b[r]
            else:
                break
        return d
