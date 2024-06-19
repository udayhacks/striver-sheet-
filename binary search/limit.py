def getFloorAndCeil(a, n, x):
    # Write your code here.

    l = 0 
    h = n-1
    ans = 0  
    while l <= h :
        m = (l+h)//2
        if a[m] == x :
            return [a[m],a[m]]
        
        if a[m] > x :
            h = m-1
        else:
            l = m+1

    f = -1 
    c = -1
    if l <n :
        c = a[l] 
    if h >= 0 :
        f = a[h]
    return [f,c]
        
    
    
a = [1,3,4]
getFloorAndCeil(a,len(a),2)