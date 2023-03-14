import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from copy import deepcopy

def go(_mat,d,cnt):
    if cnt==5:return 0
    largest=float('-inf')
    mat=deepcopy(_mat)
    if d==0:
        for x in range(n):
            target_y=0
            for y in range(n):
                largest=max(largest,mat[y][x])
                if y==0:continue
                if mat[y][x]==0:continue
                if mat[target_y][x]==0 and mat[y][x]!=0:mat[target_y][x],mat[y][x]=mat[y][x],mat[target_y][x]
                elif mat[target_y][x]==mat[y][x]!=0:mat[target_y][x]*=2;largest=max(largest,mat[target_y][x]);mat[y][x]=0;target_y+=1
                elif mat[target_y][x]!=mat[y][x]!=0:target_y+=1;mat[target_y][x],mat[y][x]=mat[y][x],mat[target_y][x]
    elif d==1:
        for y in range(n):
            target_x=n-1
            for x in range(n-1,-1,-1):
                largest=max(largest,mat[y][x])
                if x==n-1:continue
                if mat[y][x]==0:continue
                if mat[y][target_x]==0 and mat[y][x]!=0:mat[y][target_x],mat[y][x]=mat[y][x],mat[y][target_x]
                elif mat[y][target_x]==mat[y][x]!=0:mat[y][target_x]*=2;largest=max(largest,mat[y][target_x]);mat[y][x]=0;target_x-=1
                elif mat[y][target_x]!=mat[y][x]!=0:target_x-=1;mat[y][target_x],mat[y][x]=mat[y][x],mat[y][target_x]
    elif d==2:
        for x in range(n):
            target_y=n-1
            for y in range(n-1,-1,-1):
                largest=max(largest,mat[y][x])
                if y==n-1:continue
                if mat[y][x]==0:continue
                if mat[target_y][x]==0 and mat[y][x]!=0:mat[target_y][x],mat[y][x]=mat[y][x],mat[target_y][x]
                elif mat[target_y][x]==mat[y][x]!=0:mat[target_y][x]*=2;largest=max(largest,mat[target_y][x]);mat[y][x]=0;target_y-=1
                elif mat[target_y][x]!=mat[y][x]!=0:target_y-=1;mat[target_y][x],mat[y][x]=mat[y][x],mat[target_y][x]
    else:
        for y in range(n):
            target_x=0
            for x in range(n):
                largest=max(largest,mat[y][x])
                if x==0:continue
                if mat[y][x]==0:continue
                if mat[y][target_x]==0 and mat[y][x]!=0:mat[y][target_x],mat[y][x]=mat[y][x],mat[y][target_x]
                elif mat[y][target_x]==mat[y][x]!=0:mat[y][target_x]*=2;largest=max(largest,mat[y][target_x]);mat[y][x]=0;target_x+=1
                elif mat[y][target_x]!=mat[y][x]!=0:target_x+=1;mat[y][target_x],mat[y][x]=mat[y][x],mat[y][target_x]
    for i in range(4):
        largest=max(largest,go(mat,i,cnt+1))
    return largest

if __name__=="__main__":
    n=int(input())
    mat=[list(map(int,input().split())) for _ in range(n)]
    res=float('-inf')
    for i in range(4):
        res=max(res,go(mat,i,0))
    print(res)