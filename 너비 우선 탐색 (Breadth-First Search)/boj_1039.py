import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
from copy import deepcopy
input=sys.stdin.readline

def solution(n,k):
    answer=-1
    que=deque()
    que.append((n,0))
    ch=set()
    ch.add((str(n),0))
    while que:
        num,cnt=que.popleft()
        if cnt==k:answer=max(answer,num)
        str_num=str(num)
        if cnt<k:
            for i in range(len(str_num)):
                for j in range(i+1,len(str_num)):
                    if i==0 and str_num[j]=='0':continue 
                    list_num=list(str_num)
                    list_num[i],list_num[j]=list_num[j],list_num[i]
                    new_num=''.join(list_num)
                    if (new_num,cnt+1) not in ch: ch.add((new_num,cnt+1)); que.append((int(new_num),cnt+1))
    return answer

if __name__=="__main__":
    n,k=map(int,input().split())
    print(solution(n,k))