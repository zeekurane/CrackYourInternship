class Solution:
    def calculate(self, s: str) -> int:
        
        def do(num1, num2, s):
            if s=="+":
                return num1+num2
            elif s=="-":
                return num1-num2
            elif s=="*":
                return num1*num2
            elif s=="/":
                return num1//num2
        
        eq=[]
        i=0
        while i< len(s):
            if s[i]=="*" or s[i]=="/" or s[i]=="+" or s[i]=="-":
                eq.append(s[i])
            elif s[i]!=" ":
                num=""
                while i<len(s) and "0"<=s[i]<="9":
                    num+=s[i]
                    i+=1
                i-=1
                eq.append(int(num))
            i+=1
        if len(eq)>4:
            #indexes
            i1=0
            i2=2
            i3=4
            num1=eq[i1]
            num2=eq[i2]
            num3=eq[i3]
            
            while i3<len(eq):
                num3=eq[i3]
                if (eq[i3-1]=="*" and eq[i2-1]!="/") or (eq[i3-1]=="/" and eq[i2-1]!="/"):
                    num2=do(num2, num3, eq[i3-1])
                    i3+=2
                else:
                    num1=do(num1,num2,eq[i2-1])
                    num2=num3
                    i2=i3
                    i3+=2
            return do(num1,num2,eq[i2-1])
        elif len(eq)==1:
            return eq[0]
        else:
            return do(eq[0],eq[2],eq[1])