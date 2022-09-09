import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline

def solve():
    time=0
    dy,dx=[-1,0,1,0],[0,1,0,-1]; d=1
    que=deque([(1,1)])
    while True:
        time+=1
        y,x=que[0]
        ny,nx=y+dy[d],x+dx[d]
        if 0<ny<=n and 0<nx<=n:
            if (ny,nx) in apples:que.appendleft((ny,nx)); apples.remove((ny,nx)) #사과인 경우
            else:
                if (ny,nx) in que: break
                else: que.appendleft((ny,nx));que.pop()
        else:break #벽부딫힌 경우
        
        if time in moves:
            turn=moves[time]
            if turn=="L": d=(d-1)%4
            else:d=(d+1)%4
    return time

if __name__=="__main__":
    n=int(input())
    k=int(input())
    apples=[tuple(map(int, input().split())) for _ in range(k)]
    l=int(input())
    moves=dict()
    for _ in range(l):
        sec,turn=input().split()
        moves[int(sec)]=turn
    print(solve())