import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
from copy import deepcopy
input=sys.stdin.readline

def solve():
    que=deque()
    ch=[-1]*(limit+1)
    ch[n]=0
    que.append(n)
    while que:
        num=que.popleft()
        if num==g and ch[num]<=t:
            return ch[num]
        new_num_a=num+1
        if 0<=new_num_a<=limit and ch[new_num_a]==-1:
            ch[new_num_a]=ch[num]+1
            que.append(new_num_a)
        
        new_num_b=num*2
        if limit<new_num_b:continue
        else:
            highest_num=deepcopy(new_num_b); exp=0
            while 10<=highest_num: highest_num//=10; exp+=1
            new_num_b-=pow(10,exp)
            if 0<=new_num_b<=limit and ch[new_num_b]==-1:
                ch[new_num_b]=ch[num]+1
                que.append(new_num_b)

    return 'ANG'
if __name__=="__main__":
    limit=99999
    n,t,g=map(int,input().split())
    print(solve())