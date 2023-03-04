import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

dy,dx=[-1,0,1,0],[0,1,0,-1]

def up():
    tmp=[]
    for i in range(4): tmp.append(dice[i][1])
    tmp=[tmp[-1]]+tmp[:-1]
    for i in range(4):dice[i][1]=tmp[i]
def right():
    dice[1][2],dice[3][1]=dice[3][1],dice[1][2]
    dice[1]=[dice[1][-1]]+dice[1][:-1]
def down():
    tmp=[]
    for i in range(4): tmp.append(dice[i][1])
    tmp=tmp[1:]+[tmp[0]]
    for i in range(4):dice[i][1]=tmp[i]
def left():
    dice[1][0],dice[3][1]=dice[3][1],dice[1][0]
    dice[1]=dice[1][1:]+[dice[1][0]]
    
def init():
    dice=[
        [0,2,0],
        [4,1,3],
        [0,5,0],
        [0,6,0]]
    return dice

def get_score(sy,sx):
    ret=0
    mat_num=mat[sy][sx]
    que=deque();que.append((sy,sx))
    ch=[[0]*m for _ in range(n)];ch[sy][sx]=1
    while que:
        y,x=que.popleft()
        ret+=1
        for d in range(4):
            ny,nx=y+dy[d],x+dx[d]
            if 0<=ny<n and 0<=nx<m and mat[ny][nx]==mat_num and not ch[ny][nx]:
                ch[ny][nx]=1
                que.append((ny,nx))
    return ret*mat_num

def solution():
    global k
    face=6;d=1; score=0
    y,x=0,0
    for _ in range(k):
        ny,nx=y+dy[d],x+dx[d]
        if not (0<=ny<n and 0<=nx<m):
            d=(d+2)%4
            ny,nx=y+dy[d],x+dx[d]
        if d==0:up();
        elif d==1:right()
        elif d==2:down()
        else:left()
        face=dice[3][1]
        score+=get_score(ny,nx)
        y,x=ny,nx
        if face>mat[y][x]: d=(d+1)%4
        elif face<mat[y][x]:d=(d+3)%4
    return score
    
if __name__=="__main__":
    n,m,k=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    dice=init()
    print(solution())