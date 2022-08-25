import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    dp=[[0]*n for _ in range(2)]
    dp[0][0]=mat[0][0]; dp[1][0]=mat[1][0]
    for i in range(1,n):
        dp[0][i]=max(dp[0][i-1]-mat[0][i-1],dp[1][i-1])+mat[0][i]
        dp[1][i]=max(dp[1][i-1]-mat[1][i-1],dp[0][i-1])+mat[1][i]
    res=float('-inf')
    for y in range(2):
        for x in range(n):
            res=max(res,dp[y][x]) 
    return res

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        mat=[list(map(int,input().split())) for _ in range(2)]
        print(solve())