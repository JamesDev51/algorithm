import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def get_direction(dy,dx):
    if dy==-1 and dx==0:return 0
    elif dy==0 and dx==1: return 1
    elif dy==1 and dx==0:return 2
    return 3

if __name__=="__main__":
    n,k,r=map(int,input().split())
    mat=[[[0]*4 for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(r):
        y1,x1,y2,x2=map(int,input().split())
        dy1,dx1=y2-y1,x2-x1
        mat[y1][x1][get_direction(dy1,dx1)]=1
        
        dy2,dx2=y1-y2,x1-x2
        mat[y2][x2][get_direction(dy2,dx2)]=1
    cow_mat=[[0]*(n+1) for _ in range(n+1)]
    for _ in range(k):
        y,x=map(int,input().split())
        cow_mat[y][x]=1

    cow_island=[]
    que=deque()
    ch=[[0]*(n+1) for _ in range(n+1)]
    for yy in range(1,n+1):
        for xx in range(1,n+1):
            if not ch[yy][xx]:
                cows=0
                ch[yy][xx]=1
                que.append((yy,xx))
                while que:
                    y,x=que.popleft()
                    if cow_mat[y][x]:cows+=1
                    for idx,dy,dx in zip([0,1,2,3],[-1,0,1,0],[0,1,0,-1]):
                        ny,nx=y+dy,x+dx
                        if 1<=ny<=n and 1<=nx<=n and not ch[ny][nx] and not mat[y][x][idx]:
                            ch[ny][nx]=1
                            que.append((ny,nx))
                cow_island.append(cows)
    answer=0
    for i in range(len(cow_island)):
        for j in range(i+1,len(cow_island)):
            answer+=cow_island[i]*cow_island[j]
    
    print(answer)
                
        