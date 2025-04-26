class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output=[]
        for r in range(1,n+1):
            if r%3==0 and r%5!=0:
                output+=["Fizz"]
            elif r%5==0 and r%3!=0:
                output+=["Buzz"]
            elif r%3==0 and r%5==0:
                output+=["FizzBuzz"]
            else:
                output+=[str(r)]
        return output