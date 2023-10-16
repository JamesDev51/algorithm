import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque
from copy import deepcopy

if __name__=="__main__":
    mat=[list(input().strip()) for _ in range(8)]
    wall_que1=deque()
    wall_que2=deque()
    oj_que1=deque([(7,0)])
    oj_que2=deque()
    for y in range(7,-1,-1):
        for x in range(8):
            if mat[y][x]=='#':wall_que1.append((y,x))
    while oj_que1 or oj_que2:
        ch=[[0]*8 for _ in range(8)]
        while oj_que1:
            oy,ox=oj_que1.popleft()
            if oy==0 and ox==7:
                print(1)
                exit(0)
            if mat[oy][ox]=='#':continue
            for dy,dx in zip([0,-1,-1,0,1,1,1,0,-1],[0,0,1,1,1,0,-1,-1,-1]):
                ny,nx=oy+dy,ox+dx
                if 0<=ny<8 and 0<=nx<8 and mat[ny][nx]!='#' and not ch[ny][nx]:
                    ch[ny][nx]=1
                    oj_que2.append((ny,nx))
        oj_que1=deepcopy(oj_que2)
        oj_que2.clear()
        
        while wall_que1:
            wy,wx=wall_que1.popleft()
            ny,nx=wy+1,wx
            mat[wy][wx]='.'
            if ny==8:continue
            mat[ny][nx]='#'
            wall_que2.append((ny,nx))
        wall_que1=deepcopy(wall_que2)
        wall_que2.clear()
    print(0)