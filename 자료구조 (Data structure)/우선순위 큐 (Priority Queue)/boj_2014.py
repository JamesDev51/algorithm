import sys
sys.stdin = open("input.text",  "rt")
import sys
import heapq
input=sys.stdin.readline


if __name__=="__main__":
    k,n=map(int,input().split())
    primes=list(map(int,input().split()))

    heap=[]
    for prime in primes: heapq.heappush(heap,prime)
    
    prev=1; cnt=0
    while True:
        while prev==heap[0]:heapq.heappop(heap)
        prev=heapq.heappop(heap)
        cnt+=1
        
        for prime in primes:
            heapq.heappush(heap,prime*prev)
            if prev%prime==0:break
        if cnt==n:print(prev);exit()
        