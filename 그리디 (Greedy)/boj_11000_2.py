import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from heapq import heappush, heappop
def solve():
    heap=[float('inf')]
    cnt=0
    for s,e in timelist:
        if s<heap[0]:
            cnt+=1
            heappush(heap,e)
        else:
            heappop(heap)
            heappush(heap,e)
    return cnt
        

if __name__=="__main__":
    n=int(input())
    timelist=list(list(map(int,input().split())) for _ in range(n))
    timelist.sort()
    print(solve())