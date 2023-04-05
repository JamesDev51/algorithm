import sys
sys.stdin=open("input.text","rt")
from collections import deque

def go():
    num_set=set()
    offset=n//4
    for _ in range(offset):
        for s_idx in range(0,n,offset):
            num=''
            for i in range(s_idx,s_idx+offset):num+=que[i]
            num_set.add(num)
        que.append(que.popleft())
    num_list=list(num_set)
    num_list.sort(reverse=True)
    return num_list[k-1]

for t in range(1,int(input())+1):
    n,k=map(int,input().split())
    que=deque(list(input().strip()))
    print(f"#{t} {int(go(),16)}")