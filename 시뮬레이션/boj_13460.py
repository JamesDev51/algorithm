import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque
from copy import deepcopy

def serialize(mat):
    s=""
    for q in mat:s+=''.join(q)
    return s

def go(_mat):
    ret=float('inf')
    que=deque()
    que.append((_mat,1))
    while que:
        mat,level=que.popleft()
        if level==11:continue
        serialized_mat=serialize(mat)
        if serialized_mat in used:continue
        used.add(serialized_mat)

        cp_mat=deepcopy(mat)
        red_hole_in=False;blue_hole_in=False
        for x in range(1,m-1):
            dest_y=1
            for y in range(1,n-1):
                if cp_mat[y][x]=='#':dest_y=y+1
                elif cp_mat[y][x]=='O': dest_y=y
                elif cp_mat[y][x] == 'R':
                    if cp_mat[dest_y][x]=='O': cp_mat[y][x]='.';red_hole_in=True
                    else:cp_mat[y][x],cp_mat[dest_y][x]=cp_mat[dest_y][x],cp_mat[y][x];dest_y+=1
                elif cp_mat[y][x]=='B':
                    if cp_mat[dest_y][x]=='O': cp_mat[y][x]='.';blue_hole_in=True
                    else:cp_mat[y][x],cp_mat[dest_y][x]=cp_mat[dest_y][x],cp_mat[y][x];dest_y+=1
        if red_hole_in and not blue_hole_in:return level
        elif blue_hole_in:pass
        else:que.append((cp_mat,level+1))
        

        cp_mat=deepcopy(mat)
        red_hole_in=False;blue_hole_in=False
        for y in range(1,n-1):
            dest_x=m-2
            for x in range(m-2, 0, -1):
                if cp_mat[y][x]=='#':dest_x=x-1
                elif cp_mat[y][x]=='O': dest_x=x
                elif cp_mat[y][x] == 'R':
                    if cp_mat[y][dest_x]=='O': cp_mat[y][x]='.';red_hole_in=True
                    else:cp_mat[y][x],cp_mat[y][dest_x]=cp_mat[y][dest_x],cp_mat[y][x];dest_x-=1
                elif cp_mat[y][x]=='B':
                    if cp_mat[y][dest_x]=='O': cp_mat[y][x]='.';blue_hole_in=True
                    else:cp_mat[y][x],cp_mat[y][dest_x]=cp_mat[y][dest_x],cp_mat[y][x];dest_x-=1     
        if red_hole_in and not blue_hole_in:return level
        elif blue_hole_in:pass
        else:que.append((cp_mat,level+1))

        cp_mat=deepcopy(mat)
        red_hole_in=False;blue_hole_in=False
        for x in range(1,m-1):
            dest_y=n-2
            for y in range(n-2,0,-1):
                if cp_mat[y][x]=='#':dest_y=y-1
                elif cp_mat[y][x]=='O': dest_y=y
                elif cp_mat[y][x] == 'R':
                    if cp_mat[dest_y][x]=='O': cp_mat[y][x]='.';red_hole_in=True
                    else:cp_mat[y][x],cp_mat[dest_y][x]=cp_mat[dest_y][x],cp_mat[y][x];dest_y-=1
                elif cp_mat[y][x]=='B':
                    if cp_mat[dest_y][x]=='O': cp_mat[y][x]='.';blue_hole_in=True
                    else:cp_mat[y][x],cp_mat[dest_y][x]=cp_mat[dest_y][x],cp_mat[y][x];dest_y-=1
        if red_hole_in and not blue_hole_in:return level
        elif blue_hole_in:pass
        else:que.append((cp_mat,level+1))

        cp_mat=deepcopy(mat)
        red_hole_in=False;blue_hole_in=False
        for y in range(1,n-1):
            dest_x=1
            for x in range(1,m-1):
                if cp_mat[y][x]=='#':dest_x=x+1
                elif cp_mat[y][x]=='O': dest_x=x
                elif cp_mat[y][x] == 'R':
                    if cp_mat[y][dest_x]=='O': cp_mat[y][x]='.';red_hole_in=True
                    else:cp_mat[y][x],cp_mat[y][dest_x]=cp_mat[y][dest_x],cp_mat[y][x];dest_x+=1
                elif cp_mat[y][x]=='B':
                    if cp_mat[y][dest_x]=='O': cp_mat[y][x]='.';blue_hole_in=True
                    else:cp_mat[y][x],cp_mat[y][dest_x]=cp_mat[y][dest_x],cp_mat[y][x];dest_x+=1
        if red_hole_in and not blue_hole_in:return level
        elif blue_hole_in:pass
        else:que.append((cp_mat,level+1))
    return ret

if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[list(input().strip()) for _ in range(n)]
    used=set()
    res=go(mat)
    print(res if res!=float('inf') else -1)
    