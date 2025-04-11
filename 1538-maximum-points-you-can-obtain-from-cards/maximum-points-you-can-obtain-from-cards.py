class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_sum=sum(cardPoints[:k])
        total_sum=max_sum
        for r in range(1,k+1):
            max_sum=max_sum-cardPoints[k-r]+cardPoints[-r]
            total_sum=max(total_sum,max_sum)
        return total_sum