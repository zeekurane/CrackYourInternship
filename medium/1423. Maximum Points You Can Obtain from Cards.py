class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints)==k:
            return sum(cardPoints)
        else:
            total_sum=0
            for i in range(k):
                total_sum+=cardPoints[i]
            max_score=total_sum
            for i in range(k):
                total_sum+=cardPoints[-i-1]-cardPoints[k-1-i]
                if total_sum>max_score:
                    max_score=total_sum
            return max_score