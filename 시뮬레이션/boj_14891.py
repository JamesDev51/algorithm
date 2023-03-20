import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque


if __name__=="__main__":
    topnis=[]
    for _ in range(4):
        topni=deque(input().strip())
        topnis.append(topni)
    move_que=deque()
    for _ in range(int(input())):
        move_que.clear()
        idx,direction = map(int,input().split())
        idx-=1
        move_que.append((idx,direction))
            
        last_direction=direction
        for left_idx in range(idx-1,-1,-1):
            if topnis[left_idx+1][6]!=topnis[left_idx][2]:
                if last_direction==1:last_direction=-1 #시계 -> 반시계    
                else:last_direction=1 #반시계 -> 시계
                move_que.append((left_idx,last_direction))
            else:break
        last_direction=direction
        for  right_idx in range(idx+1,4):
            if topnis[right_idx-1][2]!=topnis[right_idx][6]:
                if last_direction==1:last_direction=-1 #시계 -> 반시계
                else:last_direction=1 #반시계 -> 시계
                move_que.append((right_idx,last_direction))
            else:break
        while move_que:
            idx,direction=move_que.popleft()
            if direction==1:topnis[idx].appendleft(topnis[idx].pop()) #시계
            else:topnis[idx].append(topnis[idx].popleft()) #반시계
        
    res=0
    if topnis[0][0]=='0':res+=0
    else:res+=1
    if topnis[1][0]=='0':res+=0
    else:res+=2
    if topnis[2][0]=='0':res+=0
    else:res+=4
    if topnis[3][0]=='0':res+=0
    else:res+=8
    print(res)