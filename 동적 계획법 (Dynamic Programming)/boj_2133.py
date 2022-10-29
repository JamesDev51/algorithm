import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

    

if __name__=="__main__":
    n=int(input())
    dp=[0]*(n+2)
    dp[2]=3
    for i in range(4,n+1,2):
        dp[i]+=dp[i-2]*3
        for j in range(i-4,0,-2): dp[i]+=2*dp[j]
        dp[i]+=2
    
    print(dp[n])