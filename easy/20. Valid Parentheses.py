class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        relation={"(":")","{":"}","[":"]"}
        for bracket in s:
            if bracket in relation:
                stack.append(bracket)
            elif len(stack)==0 or relation[stack.pop()]!=bracket:
                return False
        return len(stack)==0