import sys
sys.stdin = open("input.text",  "rt")
import sys
import heapq
input=sys.stdin.readline

def solve():
    cnt=0 
    heap=[float('inf')]
    for s,e in info:
        if heap[0]<=s:heapq.heappop(heap)
        else: cnt+=1
        heapq.heappush(heap,e)
    return cnt
if __name__=="__main__":
    n=int(input())
    info=[list(map(int,input().split())) for _ in range(n)]
    info.sort()
    print(solve())