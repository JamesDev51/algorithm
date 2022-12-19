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
        heapq.heappush(heap,num)
    res=0
    while len(heap)>=2:
        num1,num2=heapq.heappop(heap),heapq.heappop(heap)
        res+=(num1+num2)
        heapq.heappush(heap,num1+num2)
    print(res)