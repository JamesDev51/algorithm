import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
import heapq


if __name__=="__main__":
    n=int(input())
    heap=[]
    for _ in range(n):
        row=list(map(int, input().split()))
        for elm in row:
            if len(heap)<n: heapq.heappush(heap,elm)
            elif len(heap)==n:
                poped=heapq.heappop(heap)
                heapq.heappush(heap,max(poped,elm))
    print(heap[0])