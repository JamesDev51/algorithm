import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

snake=deque()
dy,dx=[-1,0,1,0],[0,1,0,-1]

def go():
    time=0;d=1
    snake.append((0,0))
    while True:
        y,x=snake[0] #가장 맨 앞 머리
        ny,nx=y+dy[d],x+dx[d]
        if not 0<=ny<n or not 0<=nx<n or (ny,nx) in snake:return time+1
        snake.appendleft((ny,nx)) #머리 늘리기
        if mat[ny][nx]==1:mat[ny][nx]=0
        else:snake.pop() #꼬리 줄이기
        time+=1
        
        if move_plans and time==move_plans[0][0]:
            _,div=move_plans.popleft()
            if div=="L":
                d=(d+3)%4
            else:
                d=(d+1)%4
        

if __name__=="__main__":
    n=int(input())
    mat=[[0]*n for _ in range(n)]
    for _ in range(int(input())):
        y,x=map(int,input().split())
        mat[y-1][x-1]=1
    move_plans=deque()
    for _ in range(int(input())):
        sec,div=input().split()
        move_plans.append((int(sec),div))
    print(go())