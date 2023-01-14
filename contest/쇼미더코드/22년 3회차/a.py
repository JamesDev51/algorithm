import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

def solve():
    dp1=[0]*(n+1)
    for i in range(n):
        threshold=1 if budahs[i]==1 else -1
        if i==0: dp1[i]=threshold;continue
        dp1[i]=max(0,dp1[i-1]+threshold,threshold)
    dp2=[0]*(n+1)
    for i in range(n):
        threshold=1 if budahs[i]==2 else -1
        if i==0: dp2[i]=threshold;continue
        dp2[i]=max(0,dp2[i-1]+threshold,threshold)
    return max(max(dp1),max(dp2))


if __name__=="__main__":
    n=int(input())
    budahs=list(map(int,input().split()))
    print(solve())