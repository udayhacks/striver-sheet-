#User function Template for python3
class Solution:

	def count(self,arr, n, x):
	    
	    
	    l = 0 
	    h = n -1
	    k = -1 
	    j = n 
	    
	    while l <=h  : 
	        m = (l+h)//2 
	        if x == arr[m] :
	            jj = kk = m
	            while (jj-1 > 0  and arr[jj-1] == x ) or (kk+1 < n and arr[kk+1] == x ) :
	                j = min(j,jj-1)
	                k = max(k,kk+1)
	                jj-=1
	                k+=1
	            return (k-j)+1
	            
	        elif x < arr[m] :
	           h = m-1
	        else:
	           l = m+1
	           
	           
	       
	       
	                

		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3



a = Solution()
a.count([1,2,2,2,3],5,2)