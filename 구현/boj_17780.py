import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

if __name__=="__main__":
    n,k=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    horse_mat=[[deque() for _ in range(n)] for _ in range(n)]
    dy,dx=[0,0,-1,1],[1,-1,0,0]
    horse_loc=[[0,0] for _ in range(k)]
    horse_dir=[0]*k
    for i in range(k):
        r,c,d=map(int,input().split())
        horse_mat[r-1][c-1].append(i)
        horse_loc[i]=[r-1,c-1]
        horse_dir[i]=d-1
        
    turn=0
    flag=True
    while turn<=1000 and flag:
        turn+=1
        for i in range(k):
            hy,hx=horse_loc[i] #현재 말의 위치
            b_h=horse_mat[hy][hx][0] #가장 아래의 말
            if b_h!=i:continue
            b_h_d=horse_dir[b_h]
            nhy,nhx=hy+dy[b_h_d], hx+dx[b_h_d]
            
            if not (0<=nhy<n and 0<=nhx<n) or mat[nhy][nhx]==2: #범위 벗어나거나 파란색
                #방향 변경
                if b_h_d==0:b_h_d=1
                elif b_h_d==1:b_h_d=0
                elif b_h_d==2:b_h_d=3
                elif b_h_d==3:b_h_d=2
                horse_dir[b_h]=b_h_d #새로운 방향 넣어주기
                
                nhy,nhx=hy+dy[b_h_d],hx+dx[b_h_d]
                if not (0<=nhy<n and 0<=nhx<n) or mat[nhy][nhx]==2: continue
            
            for horse in horse_mat[hy][hx]:horse_loc[horse]=[nhy,nhx] #위치 변경
            if mat[nhy][nhx]==0:
                while horse_mat[hy][hx]:horse_mat[nhy][nhx].append(horse_mat[hy][hx].popleft())
            elif mat[nhy][nhx]==1:
                while horse_mat[hy][hx]:horse_mat[nhy][nhx].append(horse_mat[hy][hx].pop())
            if len(horse_mat[nhy][nhx])>=4:
                flag=False
            
                
    print(turn if turn<=1000 else -1)
    