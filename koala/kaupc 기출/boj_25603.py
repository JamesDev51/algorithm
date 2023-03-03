import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solution():
    ans=float('inf')
    for i in range(k):
        if offers[i]<=ans:
            ans=offers[i]
            lt=rt=i+1
    min_value=float('inf')
    min_idx=-1
    while lt+k<=n:
        if rt-lt==k:
            ans=max(ans,min_value)
            lt=rt=min_idx+1
            min_value=float('inf')
            continue
        elif offers[rt]<=ans: #가다가 누적보다 작거나 같은 값 -> 윈도우 초기화
            lt=rt=rt+1
            min_value=float('inf')
            continue
        elif offers[rt]<=min_value:
            min_value=offers[rt]
            min_idx=rt
        rt+=1
    return ans
        
if __name__=="__main__":
    n,k=map(int,input().split())
    offers=list(map(int,input().split()))
    print(solution())