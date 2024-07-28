class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans=[]
        width=0
        start=[]
        end=[]
        length=[]
        i=0
        while i<len(words):
            if width>0:
                width+=1 #spacelength
            else:
                start.append(i)
            width+=len(words[i])
            if width>maxWidth:
                end.append(i-1)
                length.append(width-1-len(words[i]))
                width=0
                i-=1
            i+=1
        
        end.append(len(words)-1)
        length.append(width)
        for i in range(len(start)):
            
            if end[i]-start[i]==0 or i==len(start)-1: #left_justified
                s=words[start[i]]
                spaces=maxWidth-length[i]
                for j in range(start[i]+1, end[i]+1):
                    s+=" "+words[j]
                s+=" "*spaces
                
            else: #right_justified and left_justified
                s=words[start[i]]
                spaces=maxWidth-length[i]
                top_up=spaces%(end[i]-start[i])
                for j in range(start[i]+1, end[i]+1):
                    s+=" "*(1+(spaces//(end[i]-start[i])))
                    if top_up>0:
                        s+=" "
                        top_up-=1
                    s+=words[j]
            
            ans.append(s)
        return ans