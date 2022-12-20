import sys
sys.stdin = open("input.text",  "rt")
import sys
import heapq
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    heap=[]
    for i in range(n):
        arr=list(map(int, input().split()))
        if i==0: 
            heap=arr
            heapq.heapify(heap)
        else:
            for num in arr:
                if heap[0]<num:
                    heapq.heappop(heap)
                    heapq.heappush(heap,num)
    print(heap[0])