import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(s,e):
    if s==e: return 0
    if s+1==e: return arr[s]
    mid=(s+e)//2
    res=max(solve(s,mid),solve(mid,e))
    
    l,r=mid,mid;w=1;  h=arr[mid]
    while w<=e-s:
        p=min(h,arr[l-1]) if s<l else -1
        q=min(h,arr[r+1]) if r<e-1 else -1
        
        if p>=q:h=p; l-=1
        else:h=q; r+=1
        w+=1
        res=max(res,w*h)
    return res
if __name__=="__main__":
    n=int(input())
    arr=list(int(input()) for _ in range(n))
    print(solve(0,n))