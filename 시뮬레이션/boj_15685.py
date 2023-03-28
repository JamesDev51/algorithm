import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque
from copy import deepcopy
LIMIT=101
dy,dx=[0,-1,0,1],[1,0,-1,0]

def make_dragon_curve(y,x,d,g):
    mat[y][x]=1
    ly,lx=y+dy[d],x+dx[d]
    mat[ly][lx]=1
    que=deque()
    que.appendleft(d)
    for _ in range(1,g+1): #0세대 ~ g세대까지
        cp_que=deepcopy(que)
        for d in que:
            new_d=(d+1)%4
            ny,nx=ly+dy[new_d],lx+dx[new_d]
            mat[ny][nx]=1
            ly,lx=ny,nx
            cp_que.appendleft(new_d)
        que=cp_que
        

if __name__=="__main__":
    mat=[[0]*LIMIT for _ in range(LIMIT)]
    for _ in range(int(input())):
        x,y,d,g=map(int,input().split())
        make_dragon_curve(y,x,d,g)
    res=0
    for y in range(LIMIT-1):
        for x in range(LIMIT-1):
            if mat[y][x] and mat[y][x+1] and mat[y+1][x] and mat[y+1][x+1]:res+=1
    print(res)            