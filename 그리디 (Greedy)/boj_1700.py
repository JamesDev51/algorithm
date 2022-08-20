import sys
sys.stdin = open("input.text",  "rt")
from collections import deque
import heapq
import sys
input=sys.stdin.readline

def check_later_used(multi):
    heap=[]
    for device in multi:heapq.heappush(heap,(-use_dict[device][0]if use_dict[device] else -1e9,device))
    return heapq.heappop(heap)[1]

def solve():
    cnt=0
    multi=[]
    for i in range(k):
        device=use_seq[i]
        use_dict[device].popleft()
        if device in multi: continue
        if len(multi)<n:multi.append(device)
        else: 
            cnt+=1
            out=check_later_used(multi)
            multi.remove(out)
            multi.append(device)
    print(cnt)
            
            
            
if __name__=="__main__":
    n,k=map(int,input().split())
    use_seq=list(map(int,input().split()))
    use_dict=dict()
    for i in range(k):
        device=use_seq[i]
        if use_dict.get(device)==None:use_dict[device]=deque([i])
        else:use_dict[device].append(i)
    solve()

    '''
    꼽을 수 있으면 그냥 꼽기
    
    가장 나중에 사용하는것부터 뽑기
    1. 현재 상태에서 몇번 후에 등장하는지 체크
        가장 숫자가 큰 것을 뽑으면 됨 (dict+que) 
    '''