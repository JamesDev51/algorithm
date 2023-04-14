import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

from bisect import bisect   


if __name__=="__main__":
    n=int(input())
    coords=[list(map(int,input().split())) for _ in range(n)]
    coords.append(coords[0])
    up,down,right,left=[],[],[],[]
    for i in range(1,n+1):
        prev=coords[i-1]
        px,py=prev
        next=coords[i]
        nx,ny=next
        if px<nx:
            right.append(nx)
            left.append(px)
        elif px>nx:
            right.append(px)
            left.append(nx)
        
        if py<ny:
            up.append(ny)
            down.append(py)
        elif py>ny:
            up.append(py)
            down.append(ny)
    up.sort();down.sort()
    right.sort();left.sort()
    
    res=0
    size=len(up)
    for h in range(min(down),max(up)):
        hh=h+0.5
        poss=size-bisect(up,hh)
        minus=size-bisect(down,hh)
        res=max(res,poss-minus)
        
    for w in range(min(left),max(right)):
        ww=w+0.5
        poss=size-bisect(right,ww)
        minus=size-bisect(left,ww)
        res=max(res,poss-minus)
        
    print(res)
            