import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

MOD=1000000
if __name__=="__main__":
    n='  '+input().strip()
    dp=[0]*(len(n))
    dp[0]=1;dp[1]=1
    if n[2]=='0':print(0);exit(0)
    for i in range(2,len(n)):
        
        dp[i]=((dp[i-1]*( 1 if 1<=int(n[i])<=26 else 0  )))%MOD + (dp[i-2]*( 1 if 2<=i-1 and 1<=int(n[i-1:i+1])<=26 and  len(str(int(n[i-1:i+1])))==2 else 0))%MOD
    print(dp[-1]%MOD)
