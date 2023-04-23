import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

if __name__=="__main__":
    n,m=map(int,input().split())
    dp=[[0]*(m+1) for _ in range(n+1)]
    acc=[0]
    for i in range(1,n+1):
        num=int(input())
        acc.append(acc[i-1]+num)
    for i in range(1,m+1):dp[0][i]=float('-inf')

    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j]=dp[i-1][j] #포함하지 않는 경우 앞의 경우 가져오기
            for k in range(1,i+1):
                dp[i][j]=max(dp[i][j], acc[i] if j==1 else float('-inf'),(dp[k-2][j-1] if k>=2 else float('-inf'))+ acc[i]-acc[k-1])
    print(dp[n][m])
