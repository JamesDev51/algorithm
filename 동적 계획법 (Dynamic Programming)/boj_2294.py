import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    dp=[1e9]*(k+1); dp[0]=0
    for i in range(1,k+1):
        for coin in coins:
            if 0<=i-coin:
                dp[i]=min(dp[i],dp[i-coin]+1)
            else: continue
    return dp[k] if dp[k]!=1e9 else -1
                

if __name__=="__main__":
    n,k=map(int,input().split())
    coins=list(int(input()) for _ in range(n))
    coins.sort()
    print(solve())