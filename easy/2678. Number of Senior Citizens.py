class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans=0
        for person in details:
            if int(person[11:13])>60:
                ans+=1
        return ans