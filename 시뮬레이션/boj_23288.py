import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

dy,dx=[-1,0,1,0],[0,1,0,-1]

def up():
    tmp=[]
    for y in range(4):tmp.append(dice[y][1])
    tmp=tmp[1:]+[tmp[0]]
    for y in range(4):dice[y][1]=tmp[y]
def down():
    tmp=[]
    for y in range(4):tmp.append(dice[y][1])
    tmp=[tmp[-1]]+tmp[:-1]
    for y in range(4):dice[y][1]=tmp[y]
def right():
    dice[3][1],dice[1][2]=dice[1][2],dice[3][1]
    dice[1].insert(0,dice[1].pop())
def left():
    dice[3][1],dice[1][0]=dice[1][0],dice[3][1]
    dice[1].append(dice[1].pop(0))

def get_score(sy,sx):
    que=deque();que.append((sy,sx))
    ch=[[0]*m for _ in range(n)];ch[sy][sx]=1
    score=0; floor_number=mat[sy][sx]
    while que:
        y,x=que.popleft()
        score+=1
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<m and not ch[ny][nx] and mat[ny][nx]==floor_number:
                ch[ny][nx]=1
                que.append((ny,nx))
    return score*floor_number
            
def solution():
    d=1
    y,x=0,0
    total_score=0    
    for _ in range(k):
        
        #1번: 굴러간다, 범위 벗어나면 반대로 굴러간다.
        ny,nx=y+dy[d],x+dx[d]
        if not (0<=ny<n and 0<=nx<m):
            d=(d+2)%4
            ny,nx=y+dy[d],x+dx[d]
        if d==0:up()
        elif d==1:right()
        elif d==2:down()
        else:left()
        y,x=ny,nx
        
        #2번: 점수를 획득한다
        total_score+=get_score(y,x)
        
        #3번: 주사위와 바닥을 비교하여 이동방향을 결정
        if dice[3][1]>mat[y][x]:d=(d+1)%4
        elif dice[3][1]<mat[y][x]:d=(d+3)%4
        else:continue
    return total_score

if __name__=="__main__":
    n,m,k=map(int,input().split())
    dice=[[0,2,0],[4,1,3],[0,5,0],[0,6,0]]    
    mat=[list(map(int,input().split())) for _ in range(n)]
    print(solution())
    