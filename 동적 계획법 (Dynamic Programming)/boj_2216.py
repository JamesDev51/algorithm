import sys
sys.stdin = open("input.text",  "rt")

a,b,c=map(int,input().split())
x=input()
y=input()
n,m=len(x),len(y)
dp=[[float('-inf')]*(m+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if i==0 and j==0:continue
        if i==0:dp[i][j]=j*b;continue
        if j==0:dp[i][j]=i*b;continue
        if x[i-1]==y[j-1]:dp[i][j]=max(dp[i][j],dp[i-1][j-1]+a)
        else:dp[i][j]=max(dp[i][j],dp[i-1][j-1]+c)
        dp[i][j]=max(dp[i][j],dp[i-1][j]+b,dp[i][j-1]+b)
print(dp[-1][-1])