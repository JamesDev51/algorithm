import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def find_virus():
    virus=[]
    for y in range(n):
        for x in range(n):
            if mat[y][x]==2:virus.append((y,x))
    return virus

def check():
    global res
    que.clear()
    ch=[[-1]*n for _ in range(n)]
    for i in range(len(virus)):
        if use[i]:
            y,x=virus[i]
            ch[y][x]=0
            que.append((y,x))
    largest=float('-inf')
    while que:
        y,x=que.popleft()
        if mat[y][x]==0:largest=max(largest,ch[y][x])
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<n and 0<=nx<n and ch[ny][nx]==-1 and mat[ny][nx]!=1:
                ch[ny][nx]=ch[y][x]+1
                que.append((ny,nx))
    flag=True
    for y in range(n):
        for x in range(n):
            if mat[y][x]!=1 and ch[y][x]==-1:flag=False
    if flag:res=min(res,largest)
    
def go(idx,cnt):
    if cnt==m:
        check()
        return
    if idx==len(virus):return
    use[idx]=1;go(idx+1,cnt+1)
    use[idx]=0;go(idx+1,cnt)
    
if __name__=="__main__":
    que=deque()
    n,m=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    res=float('inf')
    virus=find_virus()
    use=[0]*len(virus)
    
    cnt=0
    for y in range(n):
        for x in range(n):
            if mat[y][x]==0:cnt+=1
    if cnt==0:print(0)
    else:
        go(0,0)
        print(res if res!=float('inf') else -1)