"""
3047. Find the Largest Area of 
Square Inside Two Rectangles

bottomLeft =[[1,1],[2,2],[3,1]]
topRight = [[3,3],[4,4],[6,6]]
"""
from typing import List

class Solution:
    def largestSquareArea(self, 
                          bottomLeft: List[List[int]], 
                          topRight: List[List[int]]) -> int:
        
        s = 0
        n = len(bottomLeft)
        for i in range(n):
            for j in range(i+1,n):
                minX = max(bottomLeft[i][0],bottomLeft[j][0])
                maxX = min(topRight[i][0],topRight[j][0])
                minY = max(bottomLeft[i][1],bottomLeft[i][1])
                maxY = min(topRight[i][1],topRight[j][1])
                if minX <maxX and minY <maxY:
                    len_x = min(maxX - minX, maxY - minY)
                    s = max(s,len_x)

        return s*s
    
if __name__ == "__main__":
    bottomLeft =[[1,1],[2,2],[3,1]]
    topRight = [[3,3],[4,4],[6,6]]
    cls_obj = Solution()
    res = cls_obj.largestSquareArea(bottomLeft,topRight)
    print(res)