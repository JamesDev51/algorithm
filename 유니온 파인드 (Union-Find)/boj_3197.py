import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    while que:
        y,x=que.popleft()
        que2.append((y,x))
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<r and 0<=nx<c and not ch[ny][nx] and mat[ny][nx] in ['L','.']:
                ch[ny][nx]=ch[y][x]
                que.append((ny,nx))

def init():
    global unionIdx
    for y in range(r):
        for x in range(c):
            if mat[y][x]=='L' and ch[y][x]==0:
                ch[y][x]=unionIdx
                que.append((y,x))
                parents[unionIdx]=unionIdx
                bfs() 
                unionIdx+=1
    
    for y in range(r):
        for x in range(c):
            if mat[y][x]=='.' and ch[y][x]==0:
                ch[y][x]=unionIdx
                que.append((y,x))
                parents[unionIdx]=unionIdx
                bfs() 
                unionIdx+=1
    

def getParents(node):
    if parents[node]==node: return node
    parents[node]=getParents(parents[node])
    return parents[node]

def unionParents(y1,x1,y2,x2):
    global unionIdx
    N1=getParents(ch[y1][x1])
    N2=getParents(ch[y2][x2])
    if N1<N2: parents[N2]=N1
    else: parents[N1]=N2
    unionIdx-=1  

def checkParentsEqual(n1,n2):
    return getParents(n1)==getParents(n2)

def bfs_2():
    while que:
        y,x=que.popleft()
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<r and 0<=nx<c and mat[ny][nx]=='X' and ch[ny][nx]==0: #전파 안된 빙하
                ch[ny][nx]=ch[y][x]
                que2.append((ny,nx))
    
                
def bfs_1():
    global que,que2
    while que2:
        y,x=que2.popleft()
        que.append((y,x))
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<r and 0<=nx<c:
                if ch[ny][nx]!=0 and not checkParentsEqual(ch[y][x],ch[ny][nx]):
                    unionParents(y,x,ny,nx)

def solve():
    days=0
    while True:
        bfs_1()
        if checkParentsEqual(parents[1],parents[2]): break
        bfs_2()
        days+=1
    return days

if __name__=="__main__":
    r,c=map(int,input().split())
    mat=[list(input().strip()) for _ in range(r)]
    ch=[[0]*c for _ in range(r)]
    parents=dict()
    unionIdx=1
    que=deque()
    que2=deque()
    init()
    print(solve())
    