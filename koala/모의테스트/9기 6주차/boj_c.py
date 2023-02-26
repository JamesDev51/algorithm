import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

if __name__=="__main__":
    n=int(input())
    p=list(enumerate(map(int,input().split())))
    m=int(input())
    p.sort(key=lambda x:(-x[0],x[1]))
    res=float('-inf')
    ch=[-1]*(m+1)
    que=deque()
    que.append((0,0,0))
    while que:
        num,money,idx=que.popleft()

        while idx<n:
            if money+p[idx][1]<=m and ch[money+p[idx][1]]<10*num+p[idx][0]:
                ch[money+p[idx][1]]=10*num+p[idx][0]
                que.append((10*num+p[idx][0],money+p[idx][1],idx))
            idx+=1
    print(max(ch))
    
        
    