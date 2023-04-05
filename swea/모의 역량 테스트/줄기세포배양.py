import sys
sys.stdin=open("input.text","rt")

from collections import deque
def go():
    que=deque()
    
    spread=dict()
    power=dict()
    for y in range(n):
        for x in range(m):
            if mat[y][x]>0:
                spread[(y,x)]=0
                power[(y,x)]=mat[y][x]
                
    for sec in range(1,k+1):
        for key,value in spread.items():
            y,x=key
            if value+power[(y,x)]+1==sec:que.append((y,x))#방금 활성후 1시간 지남 -> 번식
        while que:
            y,x=que.popleft()
            for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
                ny,nx=y+dy,x+dx
                if (ny,nx) not in spread: #아직 번식이 안된 곳
                    spread[(ny,nx)]=sec
                    power[(ny,nx)]=power[(y,x)]
                else:
                    if spread[(ny,nx)]==sec:power[(ny,nx)]=max(power[(ny,nx)],power[(y,x)]) #방금 번식한 곳 -> 높은 생명력 우세
    cnt=0
    for key,value in spread.items():
        y,x=key
        if k<value+2*power[(y,x)] or k<=value:cnt+=1
    return cnt
                
for t in range(1,int(input())+1):
    n,m,k=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    print(f"#{t} {go()}")