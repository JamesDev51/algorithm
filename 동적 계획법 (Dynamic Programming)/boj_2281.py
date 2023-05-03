import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

MAX=10**3+1

if __name__=="__main__":
    n,m=map(int,input().split())
    acc=[0]*n
    for i in range(n):acc[i]=acc[i-1]+int(input())
    dp=[float('inf')]*MAX 
    dp[0]=pow(m-acc[0],2)
    for i in range(n):
        for j in range(i-1,-2,-1):
                empty=m-(acc[i]-(acc[j] if j>=0 else 0)+(i-j-1))
                if empty<0:break
                if i==n-1:
                    dp[i]=min(dp[i],(dp[j] if j>=0 else 0))
                else:
                    dp[i]=min(dp[i],(dp[j] if j>=0 else 0)+pow(empty,2))
    print(dp[n-1])