import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve(num):
    dp=[float('inf')]*(num+3)
    dp[1]=0; dp[2]=1; dp[3]=1
    if dp[num]!=float('inf'):return dp[num]
    for i in range(4,num+1):
        dp[i]=min(dp[i],dp[i-1]+1) 
        if i%3==0:dp[i]=min(dp[i],dp[i//3]+1)
        if i%2==0:dp[i]=min(dp[i],dp[i//2]+1)
    return dp[num]


if __name__=="__main__":
    n=int(input())
    print(solve(n))