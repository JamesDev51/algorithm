import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def sungu5(x,y,d1,d2):
    global ch
    for i in range(d1+1):ch[x+i][y-i]=5;ch[x+d2+i][y+d2-i]=5
    for i in range(d2+1):ch[x+i][y+i]=5;ch[x+d1+i][y-d1+i]=5
def sungu(sx,sy,lx,hx,ly,hy,div):
    cnt=mat[sx][sy]
    que.append((sx,sy))
    ch[sx][sy]=1
    while que:
        x,y=que.popleft()
        for dx,dy in zip([-1,0,1,0],[0,1,0,-1]):
            nx,ny=x+dx,y+dy
            if lx<=nx<hx and ly<=ny<hy and not ch[nx][ny]:
                ch[nx][ny]=div
                cnt+=mat[nx][ny]
                que.append((nx,ny))
    return cnt
                
def go(x,y,d1,d2):
    global ch,res
    ch=[[0]*n for _ in range(n)]

    sungu5(x,y,d1,d2)
    cnt1=sungu(0,0,0,x+d1,0,y+1,1)
    cnt2=sungu(0,n-1,0,x+d2+1,y+1,n,2)
    cnt3=sungu(n-1,0,x+d1,n,0,y-d1+d2,3)
    cnt4=sungu(n-1,n-1,x+d2+1,n,y-d1+d2,n,4)
    cnt5=0
    for x in range(n):
        for y in range(n):
            if ch[x][y] in [0,5]:cnt5+=mat[x][y]
    smallest=min(cnt1,cnt2,cnt3,cnt4,cnt5)
    largest=max(cnt1,cnt2,cnt3,cnt4,cnt5)
    res=min(res,largest-smallest)
    
if __name__=="__main__":
    n=int(input())
    mat=[list(map(int,input().split())) for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    que=deque()
    res=1e9
    for x in range(n):
        for y in range(n):
            for d1 in range(1,n):
                for d2 in range(1,n):
                    if 0<=x+d1+d2<n and 0<=y-d1 and y+d2<n:
                        go(x,y,d1,d2)
    print(res)