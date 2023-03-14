import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def move(y,x,dy,dx):
    moved_cnt=0
    while mat[y+dy][x+dx]!='#' and mat[y][x]!='O':
        y,x=y+dy,x+dx
        moved_cnt+=1
    return y,x,moved_cnt

def bfs(ry,rx,by,bx):
    ch=[[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)];ch[ry][rx][by][bx]=1
    que=deque();que.append((ry,rx,by,bx,1))
    while que:
        ry,rx,by,bx,cnt=que.popleft()
        if cnt==11:continue
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            rny,rnx,r_moved_cnt=move(ry,rx,dy,dx)
            bny,bnx,b_moved_cnt=move(by,bx,dy,dx)
            if mat[bny][bnx]!='O':
                if mat[rny][rnx]=='O':return cnt
                if rny==bny and rnx==bnx:
                    if r_moved_cnt>b_moved_cnt:rny-=dy;rnx-=dx
                    else:bny-=dy;bnx-=dx
                if not ch[rny][rnx][bny][bnx]:
                    ch[rny][rnx][bny][bnx]=1
                    que.append((rny,rnx,bny,bnx,cnt+1))
    return -1
        

if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[list(input().strip()) for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if mat[y][x]=='R':ry,rx=y,x
            if mat[y][x]=='B':by,bx=y,x
    print(bfs(ry,rx,by,bx))