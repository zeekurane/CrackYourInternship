class Solution:
    def numberToWords(self, num: int) -> str:
        s=str(num).zfill(12)
        lst=[s[0:3],s[3:6],s[6:9],s[9:12]]
        ex=[" Billion", " Million", " Thousand", ""]
        op=""
        def check(a):
            match a:
                case "1": return "One"
                case "2": return "Two"
                case "3": return "Three"
                case "4": return "Four"
                case "5": return "Five"
                case "6": return "Six"
                case "7": return "Seven"
                case "8": return "Eight"
                case "9": return "Nine"
                
                case "10": return "Ten"
                case "11": return "Eleven"
                case "12": return "Twelve"
                case "13": return "Thirteen"
                case "14": return "Fourteen"
                case "15": return "Fifteen"
                case "16": return "Sixteen"
                case "17": return "Seventeen"
                case "18": return "Eighteen"
                case "19": return "Nineteen"
                
                case "20": return "Twenty"
                case "30": return "Thirty"
                case "40": return "Forty"
                case "50": return "Fifty"
                case "60": return "Sixty"
                case "70": return "Seventy"
                case "80": return "Eighty"
                case "90": return "Ninety"
                case _ :return ""
                
        def tens_check(a):
            if a[0]=="1" and 0<=int(a[1])<=9:
                return check(a)
            elif a[0]=="0":
                return check(a[1])
            else:
                if check(a[1])!="":
                    return check(a[0]+"0") + " " + check(a[1])
                else:
                    return check(a[0]+"0")
            
        for i in range(4):
            if lst[i]!="000":
                if op!="":
                    op+=" "
                op+=check(lst[i][0])
                if check(lst[i][0])!="":
                    op+=" Hundred"
                if tens_check(lst[i][1:3])!="" and check(lst[i][0])!="":
                    op+= " " 
                op+=tens_check(lst[i][1:3])
                op+= ex[i]
            if i==3 and lst[i]=="000" and op=="":
                op+="Zero"
        return op