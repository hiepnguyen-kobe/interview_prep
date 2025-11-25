# given the arr of people weight and limit weight of the boat find minimun boat to carry people
#  people 3 2 1 2 Limit : 4 -> 2 boat with 3 1 and boat with 2 2 
# sort the array and use 2 pointer techniques 
# 1 2 2 3 4 5
from typing import List
class Solution : 
    def minBoat(self, arr : List[int], lim) -> int : 
        arr.sort()
        l = 0 
        r = len(arr) - 1 
        res = 0
        while (l <= r ) : 
            if arr[l] + arr[r] > lim : 
                r -= 1 
                res+=1
            else : 
                l += 1
                r -= 1
                res+= 1
        return res

def main() : 
   sol = Solution()
   arr = [1,3,2]
   lim = 3
   res = sol.minBoat(arr,lim)

   print( res)
if __name__ == "__main__" : 
    main() 

