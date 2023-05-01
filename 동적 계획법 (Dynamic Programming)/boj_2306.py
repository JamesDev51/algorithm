import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    s=input().strip()
    n=len(s)
    dp=[[0]*n for _ in range(n)]
    for j in range(1,n):
        for i in range(j-1,-1,-1):
            if (s[i]=='a' and s[j]=='t') or (s[i]=='g' and s[j]=='c'):
                dp[i][j]=dp[i+1][j-1]+2
            for k in range(i,j):
                dp[i][j]=max(dp[i][j],dp[i][k]+dp[k+1][j])
    print(dp[0][-1])
                