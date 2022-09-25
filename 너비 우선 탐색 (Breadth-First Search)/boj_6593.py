import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def bfs():
    que=deque()
    ch=[[[-1]*c for _ in range(r)] for _ in range(l)]
    for z in range(l):
        for y in range(r):
            for x in range(c):
                if mat[z][y][x]=='S': sz,sy,sx=z,y,x
                if mat[z][y][x]=='E': ez,ey,ex=z,y,x
    que.append((sz,sy,sx))
    ch[sz][sy][sx]=0
    
    while que:
        z,y,x=que.popleft()
        for dz,dy,dx in zip([-1,1,0,0,0,0],[0,0,-1,0,1,0],[0,0,0,1,0,-1]):
            nz,ny,nx=z+dz,y+dy,x+dx
            if 0<=nz<l and 0<=ny<r and 0<=nx<c and ch[nz][ny][nx]==-1 and mat[nz][ny][nx]!='#':
                ch[nz][ny][nx]=ch[z][y][x]+1
                que.append((nz,ny,nx))
    return f"Escaped in {ch[ez][ey][ex]} minute(s)." if ch[ez][ey][ex]!=-1 else "Trapped!"
            

if __name__=="__main__":
    while True:
        l,r,c=map(int,input().split())
        if not l and not r and not c: break
        mat=[]
        for _ in range(l):
            layer_mat=[list(input().strip()) for _ in range(r)]
            mat.append(layer_mat)
            input().strip()
        print(bfs())