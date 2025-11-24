# given array = [1,8,6,2,5,7] 
#output : maximum area created by (p1 - p2)*min(height from arr) 

from typing import List 
class Solution : 
    def maxArea(self, height : List[int]) -> int : 
        maxarea = 0 
        l = 0 
        r = len(height) - 1 

        while(l < r) : 
            maxarea = max(maxarea , min(height[l],height[r])*(r-l))
            if height[l] < height[r] : 
                l+=1 
            else : 
                r-= 1 
        return maxarea
    
def main() : 
    arr = [1,8,6,2,5,7]
    sol = Solution()
    res = sol.maxArea(arr)
    print("max area : ", res) 
if __name__ == "__main__" : 
    main()
