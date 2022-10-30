import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def get_start_point():
    for y in range(n):
        for x in range(m):
            if mat[y][x]=='0': return (y,x)

def solve():
    que=deque()
    sy,sx=get_start_point()
    que.append((sy,sx,0))
    ch[sy][sx][0]=0

    res=-1
    while que:
        y,x,keys=que.popleft()
        if mat[y][x]=='1': res=ch[y][x][keys]; break
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<n and 0<=nx<m: #범위
                if mat[ny][nx] in "abcdef":
                    s_idx=ord(mat[ny][nx]) - ord('a')+1
                    if ch[ny][nx][keys | 1<<s_idx]==-1:
                        ch[ny][nx][keys | 1<<s_idx]=ch[y][x][keys]+1
                        que.append((ny,nx,keys | 1<<s_idx))
                elif mat[ny][nx] in "ABCDEF" and ch[ny][nx][keys]==-1:
                    b_idx=ord(mat[ny][nx])-ord('A')+1
                    if keys & 1<<b_idx:
                        ch[ny][nx][keys]=ch[y][x][keys]+1
                        que.append((ny,nx,keys))
                else:
                    if mat[ny][nx]!='#' and ch[ny][nx][keys]==-1:
                        ch[ny][nx][keys]=ch[y][x][keys]+1
                        que.append((ny,nx,keys))
    return res  
    
    

if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[list(input().strip()) for _ in range(n)]
    ch=[[[-1]*(1<<7) for _ in range(m)] for _ in range(n)]
    print(solve())