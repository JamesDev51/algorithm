import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    dp=[0]*(n+1);
    for i in range(n):dp[i]=arr[i]
    for i in range(1,n):
        for j in range(i):
            if arr[j]<arr[i]:dp[i]=max(dp[i], arr[i]+dp[j])
    return max(dp)
            

if __name__=="__main__":
    n=int(input())
    arr=list(map(int, input().split()))
    print(solve())