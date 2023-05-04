import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    dp=[0]*n
    for i in range(n):
        largest,smallest=arr[i],arr[i]
        for j in range(i+1,n):
            largest=max(largest,arr[j])
            smallest=min(smallest,arr[j])
            dp[j]=max(dp[j],(dp[i-1] if i-1>=0 else 0)+(largest-smallest))
    print(max(dp))