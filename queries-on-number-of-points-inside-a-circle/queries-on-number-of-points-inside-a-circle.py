class Solution(object):
    def countPoints(self, points, queries):
        result = []
        for i in queries:
            pts = 0
            for j in points:
                x2 = (j[0] - i[0]) ** 2
                y2 = (j[1] - i[1]) ** 2
                dim = i[2] ** 2
                
                if x2 + y2 <= dim:
                    pts += 1
                    
            result.append(pts)
        
        return result                    
         