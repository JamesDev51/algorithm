import sys
sys.stdin = open("input.text",  "rt")
import sys
import heapq
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    heap=[]
    for _ in range(n):
        num=int(input())
        if not num:
            print(-heapq.heappop(heap) if heap else 0)
        else:
            heapq.heappush(heap,-num)
            