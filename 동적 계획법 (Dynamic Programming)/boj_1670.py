import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

MOD=987654321
        
if __name__=="__main__":
    n=int(input())
    dp=[0]*10001
    dp[0]=1;dp[2]=1
    for i in range(4,n+1,2):
        for j in range(0,i-1,2):
            dp[i]+=(dp[j]*dp[i-2-j])%MOD
    print(dp[n]%MOD)