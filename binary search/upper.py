

import sys
def getFloorAndCeil(arr, n, x):
    c = -1
    f = -1 
    for i in arr :
        if i < x and (f==-1 or i > f):
            f  = i 
        if i  > x and (c ==-1 or i < c ) :
            c = i 
    return [f,c]

a =[5, 6, 5, 9, 6, 5, 5, 6]
x = 8
getFloorAndCeil(a,len(a),x)