import sys
sys.stdin = open("input.text",  "rt")
import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline

def go(time):
    if time>1000:
        print(-1)
        exit(0)
    
    for i in range(1,k+1):
        hy,hx=loc[i]
        d=direction[i]
        ny,nx=hy+dy[d],hx+dx[d]
        
        if (0<=ny<n and 0<=nx<n and mat[ny][nx]==2) or not 0<=ny<n or not 0<=nx<n:  #범위 벗어나거나 파랑
            if d==0:new_d=1
            elif d==1:new_d=0
            elif d==2:new_d=3
            elif d==3:new_d=2
            direction[i]=new_d
            ny,nx=hy+dy[new_d],hx+dx[new_d]
        if (0<=ny<n and 0<=nx<n and mat[ny][nx]==2) or not 0<=ny<n or not 0<=nx<n:continue

        idx=horses[hy][hx].index(i)
        move_horses=[]
        tot=len(horses[hy][hx])
        for _ in range(tot-idx):
            horse=horses[hy][hx].pop()
            loc[horse]=(ny,nx)
            move_horses.append(horse)
        if mat[ny][nx]==0: horses[ny][nx].extend(reversed(move_horses)) #흰색
        elif mat[ny][nx]==1:horses[ny][nx].extend(move_horses)  #빨간색
        
        if len(horses[ny][nx])>=4:
            print(time)
            exit(0)
    go(time+1)
    

if __name__=="__main__":
    dy,dx=[0,0,-1,1],[1,-1,0,0]
    n,k=map(int, input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    loc=[[]]*(k+1)
    direction=dict()
    horses=[[[] for _ in range(n)] for _ in range(n)]
    for idx in range(1,k+1):
        y,x,d=map(int,input().split())
        horses[y-1][x-1].append(idx)
        direction[idx]=d-1
        loc[idx]=(y-1,x-1)
    go(1)
