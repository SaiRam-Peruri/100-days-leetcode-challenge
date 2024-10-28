class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=len(word1)
        b=len(word2)
        c=""
        if a>b:
            for r in range(b):
                c+=word1[r]+word2[r]
            return c+word1[b:]
        if a<b:
            for r in range(a):
                c+=word1[r]+word2[r]
            return c+word2[a:]
        if a==b:
            for r in range(a):
                c+=word1[r]+word2[r]
            return c

        