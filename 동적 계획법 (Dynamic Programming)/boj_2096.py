import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    dp=[[[0]*2 for _ in range(3)] for _ in range(2)]
    for i in range(n):
        a,b,c=map(int,input().split())
        dp[1][0][0]=max(dp[0][0][0],dp[0][1][0])+a
        dp[1][0][1]=min(dp[0][0][1],dp[0][1][1])+a
        dp[1][1][0]=max(dp[0][0][0],dp[0][1][0],dp[0][2][0])+b
        dp[1][1][1]=min(dp[0][0][1],dp[0][1][1],dp[0][2][1])+b
        dp[1][2][0]=max(dp[0][1][0],dp[0][2][0])+c
        dp[1][2][1]=min(dp[0][1][1],dp[0][2][1])+c
        
        for j in range(3):
            for k in range(2):
                dp[0][j][k]=dp[1][j][k] 
    
    largest=float('-inf');smallest=float('inf')
    for i in range(3):
        largest=max(largest,dp[-1][i][0])
        smallest=min(smallest,dp[-1][i][1])
    print(largest,smallest)
        