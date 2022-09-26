import sys
sys.stdin = open("input.text",  "rt")
import sys
import copy
from collections import deque
input=sys.stdin.readline

def solve():
    ch=[[-1]*c for _ in range(r)]
    que=deque(); tmp_que=deque()
    water_que=deque(); tmp_water_que=deque()
    for y in range(r):
        for x in range(c):
            if mat[y][x]=='S': que.append((y,x)); ch[y][x]=0;
            if mat[y][x]=='D': ey,ex=y,x
            if mat[y][x]=='*': water_que.append((y,x))
    while que or water_que:
        while water_que:
            y,x=water_que.popleft()
            for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                ny,nx=y+dy,x+dx
                if 0<=ny<r and 0<=nx<c and mat[ny][nx] in ".S":
                    mat[ny][nx]="*"
                    tmp_water_que.append((ny,nx))
        water_que=copy.deepcopy(tmp_water_que)
        tmp_water_que.clear()
        
        while que:
            y,x=que.popleft()
            for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                ny,nx=y+dy,x+dx
                if 0<=ny<r and 0<=nx<c and mat[ny][nx] in ".D" and ch[ny][nx]==-1:
                    ch[ny][nx]=ch[y][x]+1
                    tmp_que.append((ny,nx))
        que=copy.deepcopy(tmp_que)
        tmp_que.clear()
    return ch[ey][ex] if ch[ey][ex]!=-1 else "KAKTUS"
if __name__=="__main__":
    r,c=map(int,input().split())
    mat=[list(input().strip()) for _ in range(r)]
    print(solve())