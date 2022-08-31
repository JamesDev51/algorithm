import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    dp=[[-1]*3 for _ in range(n)]
    dp[0][0]=mat[0][0]; dp[0][1]=mat[1][0];dp[0][2]=0
    
    for i in range(1,n):
        dp[i][0]=max(dp[i][0],dp[i-1][1],dp[i-1][2])+mat[0][i]
        dp[i][1]=max(dp[i][1],dp[i-1][0],dp[i-1][2])+mat[1][i]
        dp[i][2]=max(dp[i][2],dp[i-1][0],dp[i-1][1])
        
    res=float('-inf')
    for y in range(n):
        for x in range(3):
            res=max(res,dp[y][x])
        
    return res

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        mat=[list(map(int,input().split())) for _ in range(2)]
        print(solve())