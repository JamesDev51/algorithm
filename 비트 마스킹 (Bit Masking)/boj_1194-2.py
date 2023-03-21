import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def go():
    for y in range(n):
        for x in range(m):
            if mat[y][x]=='0':
                sy,sx=y,x
    ch=[[[0]*(1<<7) for _ in range(m)] for _ in range(n)]
    ch[sy][sx][0]=1
    que=deque()
    que.append((sy,sx,0,0))
    while que:
        y,x,move,key=que.popleft()
        if mat[y][x]=='1':return move
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            if 0<=ny<n and 0<=nx<m and mat[ny][nx]!='#':
                if mat[ny][nx] in "abcdef" and not ch[ny][nx][key|(1<<(ord(mat[ny][nx])-96))]:
                    ch[ny][nx][key|(1<<(ord(mat[ny][nx])-96))]=1
                    que.append((ny,nx,move+1,key|(1<<(ord(mat[ny][nx])-96))))      
                elif mat[ny][nx] in "ABCDEF" and not ch[ny][nx][key] and key&(1<<(ord(mat[ny][nx])-64)):
                    ch[ny][nx][key]=1
                    que.append((ny,nx,move+1,key))      
                elif mat[ny][nx] in ".01" and not ch[ny][nx][key]:
                    ch[ny][nx][key]=1
                    que.append((ny,nx,move+1,key))      
    return -1

if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[list(input().strip()) for _ in range(n)]
    print(go())