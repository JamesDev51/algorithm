import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(s,e):
    if s==e: return 0
    if s+1==e: return arr[s]**2
    mid=(s+e)//2
    res=max(solve(s,mid),solve(mid,e))
    l,r=mid,mid; acc_sum=arr[mid];min_val=arr[mid]

    while r-l<e-s:
        p=(acc_sum+arr[l-1])*min(min_val,arr[l-1]) if s<=l-1 else -1
        q=(acc_sum+arr[r+1])*min(min_val,arr[r+1]) if r+1<e else -1
        if p>=q:min_val=min(min_val,arr[l-1]);acc_sum+=arr[l-1];l-=1
        else: min_val=min(min_val,arr[r+1]); acc_sum+=arr[r+1]; r+=1
        res=max(res,p,q)
    return res
            
    

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    print(solve(0,n))
    