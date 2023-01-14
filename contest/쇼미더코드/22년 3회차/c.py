import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            a_c=a[i-1]; b_c=b[j-1]
            dp[i][j]=max(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]+w[a_c][b_c])
    answer=0
    for q in dp:answer=max(answer,max(q))
    return answer

if __name__=="__main__":
    n,m,c=map(int,input().split())
    w=[[0]+list(map(int,input().split())) for _ in range(c)]
    w.insert(0,[])
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(solve())