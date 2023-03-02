import sys
sys.stdin = open("input.text",  "rt")
import sys
import heapq
input=sys.stdin.readline


if __name__=="__main__":
    n,k,a,b=map(int,input().split())
    heap=[]
    for _ in range(n):heapq.heappush(heap,k)
    ans=1
    while heap:
        for _ in range(a):
            poped=heapq.heappop(heap)
            heapq.heappush(heap,poped+b)
        for i in range(n):
            heap[i]-=1
            if heap[i]==0:
                print(ans)
                exit(0)
        ans+=1