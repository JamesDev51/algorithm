import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque

def init():
    for i in range(1,k+1):
        y,x=map(int, input().split())
        y-=1; x-=1
        ch[y][x]=i
        que.append((y,x))

def getParents(idx):
    if parents[idx]==idx: return idx
    parents[idx]=getParents(parents[idx])
    return parents[idx]

def checkParentsEqual(y1,x1,y2,x2):
    return getParents(ch[y1][x1])==getParents(ch[y2][x2])

def unionParents(y1,x1,y2,x2):
    global k
    P1=getParents(ch[y1][x1])
    P2=getParents(ch[y2][x2])
    if P1==P2: return
    if P1>P2: parents[P1]=P2
    else: parents[P2]=P1
    k-=1

def bfsJoin():
    global que, que2
    while que:
        y,x=que.popleft()
        que2.append((y,x))
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<n and 0<=nx<n and not checkParentsEqual(y,x,ny,nx) and ch[ny][nx]!=0:
                unionParents(y,x,ny,nx)
def bfs():
    global que, que2
    while que2:
        y,x=que2.popleft()
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<n and 0<=nx<n and not ch[ny][nx]:
                ch[ny][nx]=ch[y][x]
                que.append((ny,nx))
            
def solve():
    global k
    year=0
    while k>1:
        bfsJoin()
        if k==1: break
        bfs()
        year+=1
    return year
        
if __name__=="__main__":
    n,k=map(int,input().split())
    parents=list(range(k+1))
    ch=[[0]*n for _ in range(n)]
    que,que2=deque(),deque();
    init()
    print(solve())