class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack=[]
        t_stack=[]
        for ch in s:
            if ch!="#":
                s_stack.append(ch)
            elif len(s_stack)>0:
                s_stack.pop(-1)
        for ch in t:
            if ch!="#":
                t_stack.append(ch)
            elif len(t_stack)>0:
                t_stack.pop(-1)
        return s_stack==t_stack