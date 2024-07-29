class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_points=0
        for i in range(len(points)-1):
            d={}
            j=i+1
            max_d=0
            while j<len(points):
                if points[i][0]==points[j][0]:
                    slope="inf"
                else:
                    slope=(points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                if slope in d:
                    d[slope]+=1
                else:
                    d[slope]=1
                if max_d<d[slope]:
                    max_d=d[slope]
                j+=1
            if max_points<max_d:
                max_points=max_d
        return max_points+1