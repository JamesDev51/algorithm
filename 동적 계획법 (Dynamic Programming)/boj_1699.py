import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    dp=[1e9]*(n+3);dp[0]=0
    square_num=1
    while True:
        if square_num**2<=n:
            for now_num in range(square_num**2,n+1):
                dp[now_num]=min(dp[now_num],dp[now_num-square_num**2]+1)
        else:break
        square_num+=1
    return dp[n]
            

if __name__=="__main__":
    n=int(input())
    print(solve())