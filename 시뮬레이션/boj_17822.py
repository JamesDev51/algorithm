import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def turn(x,d,k):
    for i in range(x,n+1,x):
        for _ in range(k):
            if d==0:pans[i].appendleft(pans[i].pop())
            else:pans[i].append(pans[i].popleft())
def remove():
    ch=[[0]*m for _ in range(n+1)]
    que=deque()
    adjs=[]
    for y in range(1,n+1):
        for x in range(m):
            if pans[y][x]==0:continue
            adj=[]
            if not ch[y][x]:
                ch[y][x]=1
                que.append((y,x))
                adj.append((y,x))
                num=pans[y][x]
                while que:
                    yy,xx=que.popleft()
                    for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                        ny,nx=yy+dy,xx+dx
                        if not 1<=ny<=n:continue
                        if nx==-1:nx=m-1
                        elif nx==m:nx=0
                        
                        if not ch[ny][nx] and num==pans[ny][nx]:
                            ch[ny][nx]=1
                            que.append((ny,nx))
                            adj.append((ny,nx))
                if len(adj)>1:adjs.append(adj)

    if adjs:
        for adj in adjs:
            for y,x in adj:pans[y][x]=0
    else:
        cnt=0;tot=0
        for i in range(1,n+1):
            for num in pans[i]:
                if num==0:continue
                tot+=num
                cnt+=1
        if cnt==0:return
        avg=tot/cnt
        for i in range(1,n+1):
            for j in range(m):
                if pans[i][j]==0 or pans[i][j]==avg:continue
                elif pans[i][j]>avg:pans[i][j]-=1
                elif pans[i][j]<avg:pans[i][j]+=1
if __name__=="__main__":
    n,m,t=map(int,input().split())
    pans=[deque(list(map(int,input().split()))) for _ in range(n)]
    pans.insert(0,deque([0]*m))
    for _ in range(t):
        x,d,k=map(int,input().split())
        turn(x,d,k)
        remove()
    res=0
    for i in range(1,n+1):res+=sum(pans[i])
    print(res)