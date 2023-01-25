import sys
sys.setrecursionlimit(10000000)

MOD=1234567
dp=[0]*100002
dp[1]=1; dp[2]=1
def fibo(num):
    if dp[num]: return dp[num]
    if num<=1:return num
    dp[num]=(fibo(num-1)+fibo(num-2))%MOD
    return dp[num]%MOD

def solution(n):
    answer = fibo(n)%MOD
    return answer