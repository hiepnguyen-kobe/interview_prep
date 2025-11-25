# [1 , 4 ,5, 3,2] [3,1,5]
# /\ find an arr  is moutain array ( len > =3)  or not if it has a ascending subarrfolow by desc subarr
from typing import List
class Solution : 
    def arrCheck(self , arr : List[int] ) -> bool : 
        peak = 0 
        p = 0 
        if len(arr) < 3 : 
            return False 
        if arr[p] > arr[p + 1] :
            return False
        p+=1      
        while p < len(arr) - 1: 
          if peak == 0 : 
            if arr[p + 1] > arr[p] : p+=1
            else :
                peak = p 
                p+=1
          else :             
             if( arr[p] < arr[p + 1]) : return False
             else : p += 1 

        return True 
                
def main() : 
   sol = Solution()
   arr = [1,3,2]
   res = sol.arrCheck(arr)
   print( res)
if __name__ == "__main__" : 
    main()