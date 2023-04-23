import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    dp=[[[float('inf')]*21 for _ in range(21)] for _ in range(21)]
    n=int(input())
    s1,s2=map(int,input().split())
    m=int(input())
    a=[int(input()) for _ in range(m)]
    dp[0][s1][s2]=0
    for i in range(1,m+1):
        use=a[i-1]
        for j in range(1,21):
            for k in range(j+1,21):
                if dp[i-1][j][k]==float('inf'):continue
                if use<j:
                    dp[i][use][k]=min(dp[i][use][k],dp[i-1][j][k]+(j-use))
                elif j<=use<=k:
                    dp[i][use][k]=min(dp[i][use][k], dp[i-1][j][k]+(use-j))
                    dp[i][j][use]=min(dp[i][j][use], dp[i-1][j][k]+(k-use))
                else:
                    dp[i][j][use]=min(dp[i][j][use],dp[i-1][j][k]+(use-k))
    res=float('inf')
    for j in range(1,21):
        for k in range(1,21):
            res=min(res,dp[m][j][k])
    print(res)
    