import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    dp=[0]*(n+1); dp[1]=arr[1]
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i]=max(dp[i], arr[i],dp[j]+dp[i-j])
        
    return dp[n]
if __name__=="__main__":
    n=int(input())
    arr=list(map(int, input().split()))
    arr.insert(0,0)
    print(solve())