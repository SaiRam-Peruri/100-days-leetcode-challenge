class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        if n==0 or n==1:
            return n
        for r in range(2,n+1):
            c=a+b
            a,b=b,c
        return c

        