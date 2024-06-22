#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        import sys 
        min_val = sys.maxsize
        ans = 0 
        
        for i , j in enumerate(arr):
            if j < min_val:
                min_val= j 
                ans = i 
            if i > 0 and arr[i] < arr[i-1] :
                return ans 
            
        return ans 
    
    
a = Solution()
a.findKRotation([1,2,3,4],4)