import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

import heapq

if __name__=="__main__":
    n=int(input())
    arr=[int(input()) for _ in range(n)]
    res=0
    while True:
        lt,rt=0,0;cnt=1
        heap=[]
        while rt<n:
            now=arr[lt]
            while lt-1>=0 and now==arr[lt-1]:
                lt-=1
                cnt+=1
            while rt+1<n and now==arr[rt+1]:
                rt+=1
                cnt+=1
            left_big=arr[lt-1] if lt-1>=0 and arr[lt-1]>now else float('inf')
            right_big=arr[rt+1] if rt+1<n and arr[rt+1]>now else float('inf')
            smaller=min(left_big,right_big)
            if smaller!=float('inf'):
                heapq.heappush(heap,(now,smaller-now,lt,rt))
            lt=rt+1;rt=lt;cnt=1
        if not heap:break
        now,plus,_lt,_rt=heapq.heappop(heap)
        for idx in range(_lt,_rt+1):arr[idx]+=plus
        res+=plus
    print(res)
        
        
        