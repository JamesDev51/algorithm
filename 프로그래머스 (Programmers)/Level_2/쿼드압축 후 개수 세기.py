import sys
sys.setrecursionlimit(10000000)
res=[0,0]

def go(y1,x1,y2,x2,arr):
    if y2-y1==1 and x2-x1==1:
        res[arr[y1][x1]]+=1
        
    else:
        s=set()
        for y in range(y1,y2):
            for x in range(x1,x2):
                s.add(arr[y][x])
        if len(s)==1:
            element=s.pop()
            res[element]+=1
        else:
            mid_y,mid_x=(y1+y2)//2,(x1+x2)//2
            go(y1,x1,mid_y,mid_x,arr)
            go(y1,mid_x,mid_y,x2,arr)
            go(mid_y,x1,y2,mid_x,arr)
            go(mid_y,mid_x,y2,x2,arr)
                
def solution(arr):
    global res
    n=len(arr)
    go(0,0,n,n,arr)
    return res