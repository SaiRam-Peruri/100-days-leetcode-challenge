class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        list_numbers=[]
        c=0
        for s in range(n):
            list_numbers+=[s]
        list_numbers[0] = list_numbers[1] = 0
        p=2
        while(p*p<=n):
            if(p!=0):
                for i in range(p*p,n,p):
                    list_numbers[i] = 0
            p+=1
        for i in list_numbers:
            if i!=0:
                c+=1
        return c