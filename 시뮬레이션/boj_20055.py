import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

def solution():
    def check():
        zero_cnt=0
        for ind,_ in up_belt:
            if ind==0:zero_cnt+=1
        for ind,_ in down_belt:
            if ind==0:zero_cnt+=1
        return zero_cnt<k
    
    turn=1
    while True:
        if up_belt[-1][1]==1:up_belt[-1][1]=0 #로봇 내리기
        
        down_belt.append(up_belt.pop())
        up_belt.appendleft(down_belt.popleft())
        if up_belt[-1][1]==1:up_belt[-1][1]=0 #로봇 내리기
        
        for i in range(n-2,-1,-1):
            if up_belt[i][1]==1 and up_belt[i+1][0]>=1 and up_belt[i+1][1]==0:
                up_belt[i][1]=0
                up_belt[i+1][0]-=1
                up_belt[i+1][1]=1
            if up_belt[-1][1]==1:up_belt[-1][1]=0 #로봇 내리기
        
        if up_belt[0][0]>0:
            up_belt[0][0]-=1
            up_belt[0][1]=1
        if not check():break
        turn+=1
    return turn
        

if __name__=="__main__":
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    up_belt=deque()
    down_belt=deque()
    for i in range(2*n):
        if i<n:up_belt.append([a[i],0])
        else:down_belt.appendleft([a[i],0])
    print(solution())
    
    