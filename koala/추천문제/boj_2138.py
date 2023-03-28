import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from copy import deepcopy
used=set()

if __name__=="__main__":
    n=int(input())
    start=list(map(int, input().strip()))
    end=list(map(int, input().strip()))
    
    res=float('inf')
    
    cp_start=deepcopy(start)
    cnt=0
    for i in range(n-1):
        if  cp_start[i]!=end[i]:
            cnt+=1
            cp_start[i]=(cp_start[i]+1)%2
            cp_start[i+1]=(cp_start[i+1]+1)%2
            if i+2<n:cp_start[i+2]=(cp_start[i+2]+1)%2
    if cp_start==end:res=min(res,cnt)
    cnt=1
    cp_start=deepcopy(start)
    cp_start[0]=(cp_start[0]+1)%2
    cp_start[1]=(cp_start[1]+1)%2

    for i in range(n-1):
        if  cp_start[i]!=end[i]:
            cnt+=1
            cp_start[i]=(cp_start[i]+1)%2
            cp_start[i+1]=(cp_start[i+1]+1)%2
            if i+2<n:cp_start[i+2]=(cp_start[i+2]+1)%2
    if cp_start==end:res=min(res,cnt)
    
    print(res if res!=float('inf') else -1)
    
    